from flask import Flask, request, jsonify
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

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save file to File System Service
    file_system_url = 'http://file-system-service:5004/save'
    response = requests.post(file_system_url, files={'file': file})
    if response.status_code != 200:
        return jsonify({'error': 'Failed to save file'}), 500

    file_path = response.json().get('file_path')
    if not file_path:
        return jsonify({'error': 'No file path returned'}), 500

    # Save video info to MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO videos (path) VALUES (%s)", (file_path,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'File uploaded successfully', 'file_path': file_path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

