from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

# Helper function to generate random users
def generate_random_users(count, start_id):
    levels = ["user", "moderator"]
    users = []
    for i in range(count):
        users.append({
            "id": start_id + i,
            "username": ''.join(random.choices(string.ascii_lowercase, k=8)),
            "firstname": ''.join(random.choices(string.ascii_uppercase, k=5)),
            "lastname": ''.join(random.choices(string.ascii_uppercase, k=7)),
            "user_level": random.choice(levels),
            "password": ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        })
    return users

# Mock user data
users = generate_random_users(150, 1) + [
    {"id": 151, "username": "admin_user", "firstname": "Admin", "lastname": "User", "user_level": "admin", "password": "admin123"}
] + generate_random_users(30, 17)

# Security settings
security_options = {
    "allow_registration": 1,
    "allow_password_reset": 1,
    "password_reset_expiry_days": 2,
    "password_reset_notification_days": 1,
    "clear_passwords_via_api_enabled": 0,
    "password_strength": "strong",
    "password_expiry_days": 90,
    "password_expiry_notification_days": 7,
    "password_history": 5
}

# Token store (mock token)
tokens = {"admin_user": "admin-token-123"}  # Admin user token

@app.route('/users', methods=['GET'])
def get_users():
    detailed = request.args.get('detailed', "0") == "1"
    user_level = request.args.get('user_level')
    clear_password = request.args.get('clear_password', "0") == "1"

    if clear_password and not security_options.get("clear_passwords_via_api_enabled"):
        return jsonify({"error": "Access to clear passwords is disabled"}), 403

    result = []
    for user in users:
        if user_level and user['user_level'] != user_level:
            continue

        user_data = {
            "id": user['id'],
            "username": user['username']
        }

        if detailed or clear_password:
            user_data.update({
                "firstname": user['firstname'],
                "lastname": user['lastname'],
                "user_level": user['user_level']
            })

        if clear_password:
            user_data["password"] = user['password']

        result.append(user_data)
    return jsonify(result[:10])


@app.route('/security', methods=['GET', 'PATCH', 'PUT'])
def security():
    if request.method == 'GET':
        return jsonify(security_options)

    if request.method in ['PATCH', 'PUT']:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Update security options
        security_options.update(data)
        return jsonify({"message": "Security settings updated", "security_options": security_options})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get('username')
    password = data.get('password')

    for user in users:
        if user['username'] == username and user['password'] == password:
            token = tokens.get(username, "invalid-token")
            return jsonify({"token": token})

    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/secret', methods=['GET'])
def secret():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Authorization header missing"}), 401

    token = auth_header.split("Bearer ")[-1].strip()
    if token == tokens.get("admin_user"):
        return jsonify({"flag": "CTF{fl4sk_1s_aw3s0m3}"}), 200

    return jsonify({"error": "Invalid token"}), 403

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
