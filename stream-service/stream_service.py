from flask import Flask, request, jsonify, send_file
import requests
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'mysql-db',
    'user': 'user',
    'password': 'password',
    'database': 'video_db'
}

@app.route('/videos', methods=['GET'])
def list_videos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(videos)

@app.route('/video/<int:video_id>', methods=['GET'])
def stream_video(video_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT path FROM videos WHERE id = %s", (video_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if not result:
        return jsonify({'error': 'Video not found'}), 404

    file_path = result['path']
    file_system_url = 'http://file-system-service:5004/get'
    response = requests.get(file_system_url, params={'file_path': file_path})
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve video'}), 500

    return send_file(response.content, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

