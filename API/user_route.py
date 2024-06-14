from flask import request, jsonify, abort
from model.user import User
from flask_restx import Resource, Namespace, fields

def user_routes(api):
    ns_user = Namespace('users', description='User operations')

    user_model = ns_user.model('User', {
        'id': fields.String(readOnly=True, description='The unique identifier of a user'),
        'email': fields.String(required=True, description='The user email'),
        'password': fields.String(required=True, description='The user password'),
        'first_name': fields.String(required=True, description='The user first name'),
        'last_name': fields.String(required=True, description='The user last name'),
        'city_id': fields.String(description='The city ID'),
        'country_id': fields.String(description='The country ID'),
        'created_at': fields.DateTime(readOnly=True, description='The date and time the user was created'),
        'updated_at': fields.DateTime(readOnly=True, description='The date and time the user was last updated'),
        'places': fields.List(fields.Nested(ns_user.model('Place', {
            'id': fields.String(readOnly=True, description='The unique identifier of a place'),
            'name': fields.String(required=True, description='The place name'),
            'description': fields.String(required=True, description='The place description'),
            'address': fields.String(required=True, description='The place address'),
            'city_id': fields.String(required=True, description='The city ID'),
            'latitude': fields.Float(required=True, description='The latitude of the place'),
            'longitude': fields.Float(required=True, description='The longitude of the place'),
            'host_id': fields.String(required=True, description='The host ID'),
            'number_of_rooms': fields.Integer(required=True, description='The number of rooms in the place'),
            'number_of_bathrooms': fields.Integer(required=True, description='The number of bathrooms in the place'),
            'price_per_night': fields.Float(required=True, description='The price per night'),
            'max_guests': fields.Integer(required=True, description='The maximum number of guests'),
            'amenity_ids': fields.List(fields.String, required=True, description='The list of amenity IDs'),
            'created_at': fields.DateTime(readOnly=True, description='The date and time the place was created'),
            'updated_at': fields.DateTime(readOnly=True, description='The date and time the place was last updated')
        }))),
        'reviews': fields.List(fields.Nested(ns_user.model('Review', {
            'id': fields.String(readOnly=True, description='The unique identifier of a review'),
            'comment': fields.String(required=True, description='The review text'),
            'rating': fields.Integer(required=True, description='The review rating'),
            'user_id': fields.String(required=True, description='The user ID'),
            'place_id': fields.String(required=True, description='The place ID'),
            'created_at': fields.DateTime(readOnly=True, description='The date and time the review was created'),
            'updated_at': fields.DateTime(readOnly=True, description='The date and time the review was last updated')
        })))
    })


    """
    def validate_user(data):
        required_fields = ['first_name', 'last_name', 'email', 'password']
        if not all(field in data for field in required_fields):
            raise ValueError('error: missing required fields')
    """
    
    @api.route('/users')
    class UserResource(Resource):
        def post(self):
            required_fields = ['first_name', 'last_name', 'email']
            data = request.get_json()
            if not all (field in data for field in required_fields):
                raise ValueError('error: missing required fields')
            user = User(data["email"], data["last_name"], data["first_name"])
            print(user.__dict__)
            return jsonify(user.__dict__), 201

        def get(self):
            users = User.get_all()
            return jsonify([user.serialize() for user in users]), 200

    @api.route('/user/{user_id}', methods=['GET'])
    class UseridResource(Resource):
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
    class UserdelResource(Resource):
        def delete_user(user_id):
                if User.delete(user_id):
                    raise ValueError('User not found')
                else:
                    abort(404)