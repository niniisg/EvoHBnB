#!/bin/python3
from flask import Flask
from API.city_enpoints import country_and_cities_routes
from API.user_route import user_routes
from API.amenities_route import amenity_routes
from flask_restx import Api


app = Flask(__name__)
api = Api(app)

country_and_cities_routes(api)
user_routes(api)
amenity_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
