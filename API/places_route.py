from flask import request, jsonify, abort
from flask_restx import Resource, Namespace
from model.place import Place


api = Namespace('places', description='Places related operations')

@api.route('/places', method=['POST'])
class PlaceResource(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data.get('name'):
            abort(400, 'The name field is required.')
        new_place = Place.create(data)
        return jsonify(new_place), 201
    
    
@api.route('/places/{place_id}', method=['GET'])
class PlacesResource(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data.get('name'):
            abort(400, 'The name field is required.')
        new_place = Place.create(data)
        return jsonify(new_place), 201
    
    
@api.route('/places/{place_id}', method=['PUT'])
class PlacesResource(Resource):
    def post(self, place_id):
        data = request.get_json()
        if not data:
            abort(400, 'No data provided.')
        update_place = place.update(place_id, data)
        if not update_place:
            abort(404, 'Place not found.')
        return jsonify(update_place), 200
    
            
@api.route('/places/{place_id}', method=['DELETE'])
class PlacesDeleteResource(Resource):
    def post(self, place_id):
        success = Place.delete(place_id)
        if not success:
            abort(404, 'Place not found.')
        return '', 204
