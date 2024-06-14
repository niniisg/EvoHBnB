from flask import request, jsonify, abort
from Model.user import User
from Persistance.DataManager import DatManager

def route_manager(app):

    users = {}

    """User Management Endpoints.""""
    @app.route('/')
    def home():
        return "Welcome!"

    @app.route('/users', methods=['POST', 'GET'])
    def manage_users():
        if request.method == 'POST':
            data = request.get_json()
            if not data:
                abort(400, "This is not a valid JSON file.")
            user = User(data['email'], data['password'], data['first_name'], data['last_name'], data['id']
            file = DataManager()
            output = file.save(user)
            return jsonify({"message": "Welcome, new user!", "user": output}) 201

        elif request.method == 'GET':
            file = DataManager()
            users = file.get_all_users()
            return jsonify(users)

    @app.route('/users/<user_id>', methods=['GET'])
    def user_details(user_id):
        file = DataManger()
        user = file.get(user_id)
        if user is None:
            abort(404, "User not found.")
        return jsonify(user)

    @app.route('/users/<user_id>', methods=['PUT'])
    def update_user(user_id):
        data = request.get_json()
        if not dat:
            abort(400, "This is not a valid JSON file.")
        file = DataManager()
        user = file.get(user_id)
        if user is None:
            abort(404, "User not found.")
        # Update user details.
        user.update(data)
        file.save(user)
        return jsonify({"message": "User updated successfully.", "user": user})

    @app.route('/users/<user_id>', methods=['DELETE'])
    def delete_user(user_id):
        file = DataManager()
        user = file.get(user_id)
        if user is None:
            abort(404, "User not found.")
        file.delete(user_id)
        return jsonify({"message": "user deleted successfully."})

app = Flask(__name__)
route_manager(app)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
