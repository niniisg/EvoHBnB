from flask import request, jsonify, abort
from flask_restx import Resource, fields
from model.amenity import Amenity

def amenity_routes(api):
    @api.route('/amenities', methods=['POST'])
    class AmenityResource(Resource):
        def post(self):
                data = request.get_json()
                if not data or not data.get('name'):
                    abort(400, 'The name field is required.')
                new_amenity = Amenity.create(data)
                return jsonify(new_amenity), 201

    @api.route('/amenities', methods=['GET'])
    class AmenityResource(Resource):
        def get(self):
                amenities = Amenity.get_all()
                return jsonify(amenities)

    @api.route('/amenities/<int:amenity_id>', methods=['GET', 'PUT', 'DELETE'])
    class AmenityByIdResource(Resource):
        def get(self, amenity_id):
            if request.method == 'GET':
                amenity = Amenity.get_by_id(amenity_id)
                if not amenity:
                    abort(404, 'Amenity not found.')
                return jsonify(amenity), 200

            if request.method == 'PUT':
                    amenity = Amenity.get_by_id(amenity_id)
                    if not amenity:
                        abort(404, 'Amenity not found.')
                    updated_data = request.get_json()
                    success = Amenity.update(amenity_id, updated_data)
                    if not success:
                        abort(400, 'Update failed.')
                    updated_amenity = Amenity.get_by_id(amenity_id)
                    return jsonify(updated_amenity), 200

            if request.method == 'DELETE':
                success = Amenity.delete(amenity_id)
                if not success:
                    abort(400, 'Deletion failed.')
                return '', 204
