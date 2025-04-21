from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

todos = [
    {"id": 1, "title": "Buy groceries", "username": "alice"},
    {"id": 2, "title": "Read book", "username": "bob"},
    {"id": 3, "title": "Write blog", "username": "alice"},
]

USER_SERVICE_URL = "http://localhost:5000/users"

@app.route('/todos', methods=['GET'])
def get_todos():
    username = request.args.get('username')
    if username:
        return jsonify([todo for todo in todos if todo['username'] == username])
    return jsonify(todos)

@app.route('/projects', methods=['GET'])
def get_projects():
    username = request.args.get('username')
    if username:
        user_resp = requests.get(USER_SERVICE_URL, params={'username': username})
        if user_resp.ok and user_resp.json():
            return jsonify([todo for todo in todos if todo['username'] == username])
        return jsonify({"error": "User not found"}), 404
    return jsonify(todos)

if __name__ == '__main__':
    app.run(port=5001)
