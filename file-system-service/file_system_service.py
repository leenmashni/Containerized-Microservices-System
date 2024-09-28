from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# File storage directory
UPLOAD_FOLDER = '/files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/save', methods=['POST'])
def save_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    return jsonify({'file_path': file_path})

@app.route('/get', methods=['GET'])
def get_file():
    file_path = request.args.get('file_path')
    if not file_path or not os.path.isfile(file_path):
        return jsonify({'error': 'File not found'}), 404

    return jsonify({'file_path': file_path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

