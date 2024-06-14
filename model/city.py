from flask import Flask
from flask_restx import Api
from .BaseModel import BaseModel


class City(BaseModel):
    def __init__(self, name, country_code):
        self.city_name = name
        self.country_code = country_code
        super().__init__()
        
        

def city_name(self, city_name):
    if city_name == "":
        return "City name cannot be empty"
    self.city_name.append(city_name)
    return self.city_name
