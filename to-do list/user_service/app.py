from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "username": "alice"},
    {"id": 2, "username": "bob"},
    {"id": 3, "username": "carol"}
]

@app.route('/users', methods=['GET'])
def get_users():
    username = request.args.get('username')
    if username:
        return jsonify([user for user in users if user['username'] == username])
    return jsonify(users)

if __name__ == '__main__':
    app.run(port=5000)
