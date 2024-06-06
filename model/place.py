#!/usr/bin/python3

class Place:
    def __init__(self, place_id, name, host):
        self.place_id = place_id
        self.name = name
        self.host = host
        self.reviews = []
    def add_review(self, review):
        self.reviews.append(review)
    def validate_one_host_per_place(self, place_dao):
        existing_place = place_dao.get_place_by_id(self.place_id)
        if existing_place and existing_place.host != self.host:
            return False
        return True
