from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory us-er data storage
users = {}

# Home route
@app.route('/')
def home():
    return "Welcome to the User Management API!"

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user}), 200
    return jsonify({"error": "User not found"}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    user_id = max(users.keys(), default=0) + 1
    users[user_id] = {"name": data['name']}
    return jsonify({"message": "User created", "user_id": user_id}), 201

# Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    users[user_id]['name'] = data['name']
    return jsonify({"message": "User updated"}), 200

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
    