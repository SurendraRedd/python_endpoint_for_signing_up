from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory user storage (for demonstration purposes)
# In production, use a database
users = []

def is_strong_password(password):
    """Checks if the provided password is strong."""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if not is_strong_password(password):
        return jsonify({'error': 'Password is not strong enough'}), 400

    # Check if username already exists
    if any(user['username'] == username for user in users):
        return jsonify({'error': 'Username already exists'}), 400

    # Store the new user
    users.append({'username': username, 'password': password})
    return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
