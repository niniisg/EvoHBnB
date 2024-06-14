from flask import request, jsonify, abort
from model.user import User
from flask_restx import Resource


def user_routes(api):

    """
    def validate_user(data):
        required_fields = ['first_name', 'last_name', 'email', 'password']
        if not all(field in data for field in required_fields):
            raise ValueError('error: missing required fields')
    """
    
    @api.route('/users', methods=['POST'])
    class UserResource(Resource):
        def create_user():
            required_fields = ['first_name', 'last_name', 'email', 'password']
            data = request.get_json()
            if not all (field in data for field in required_fields):
                raise ValueError('error: missing required fields')
            user = User.create(data)
            return jsonify(user.serialize()), 201

    @api.route('/users', methods=['GET'])
    class UserResource(Resource):
        def get_user():
            users = User.get_all()
            return jsonify([user.serialize() for user in users]), 200

    @api.route('/user/{user_id}', methods=['GET'])
    class UserResource(Resource):
        def get_user(user_id):
            user = User.get_by_id(user_id)
            if user:
                return jsonify(user.serialize()), 200
            else:
                abort(404)
            
    @api.route('/users/{user_id}', methods=['PUT'])
    class UserResource(Resource):
        def update_user(user_id):
            required_fields = ['first_name', 'last_name', 'email', 'password']
            data = request.get_json()
            if not all(field in data for field in required_fields):
                raise ValueError('error: missing required fields')
            if User.update(user_id, data):
                return '', 204
            else:
                abort(404)
            
    @api.route('/users/{user_id}', methods=['DELETE'])
    class UserResource(Resource):
        def delete_user(user_id):
                if User.delete(user_id):
                    raise ValueError('User not found')
                else:
                    abort(404)