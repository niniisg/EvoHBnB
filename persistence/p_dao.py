#!/usr/bin/python3

class PlaceDAO:
    def __init__(self):
        self.places = []

    def save_place(self, place):
        self.places.append(place)

    def get_place_by_id(self, place_id):
        for place in self.places:
            if place.place_id == place_id:
                return place
        return None
