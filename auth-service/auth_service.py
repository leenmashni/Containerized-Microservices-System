from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple authentication mock
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    if users.get(username) == password:
        return jsonify({'message': 'Authenticated successfully'})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

