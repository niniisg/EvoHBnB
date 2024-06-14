from flask import request, jsonify
from flask_restx import Resource, fields
from model.country import Country
from model.city import City



def country_and_cities_routes(api):
    country_model = api.model('Country', {
        'code': fields.String,
        'name': fields.String,
        'population': fields.Integer,
        
    })

    city_model = api.model('City', {
        'id': fields.Integer,
        'name': fields.String,
        'country_code': fields.String,
        'population': fields.Integer,
    })

    @api.route('/countries/<string:country_code>')
    class CountryByCodeResource(Resource):
        def get(self, country_code):
            country = Country.get_by_code(country_code)
            if country:
                return api.marshal(country, country_model)
            else:
                return {'error': 'Country not found'}, 404

    @api.route('/countries/<string:country_code>/cities')
    class CitiesByCountryResource(Resource):
        def get(self, country_code):
            cities = Country.get_cities_by_country_code(country_code)
            if cities:
                return api.marshal(cities, city_model)
            else:
                return {'error': 'No cities found for the given country code'}, 404

    @api.route('/cities')
    class CityResource(Resource):
        @api.expect(city_model)
        def post(self):
            data = request.json
            city = City.create(data)
            if city:
                return api.marshal(city, city_model), 201
            else:
                return {'error': 'Failed to create city'}, 500

        def get(self):
            cities = City.get_all()
            return api.marshal(cities, city_model), 200

    @api.route('/cities/<int:city_id>')
    class CityByIdResource(Resource):
        def get(self, city_id):
            city = City.get_by_id(city_id)
            if city:
                return api.marshal(city, city_model), 200
            else:
                return {'error': 'City not found'}, 404

        @api.expect(city_model)
        def put(self, city_id):
            data = request.json
            city = City.update(city_id, data)
            if city:
                return api.marshal(city, city_model), 200
            else:
                return {'error': 'Failed to update city'}, 500

        def delete(self, city_id):
            success = City.delete(city_id)
            if success:
                return {'message': 'City deleted successfully'}, 200
            else:
                return {'error': 'City not found'}, 404
