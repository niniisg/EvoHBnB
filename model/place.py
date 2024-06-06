#!/usr/bin/python3

class Place:
    def __init__(self, place_id, name, host):
        self.place_id = place_id
        self.name = name
        self.host = host
        self.reviews = []
    def add_review(self, review):
        self.reviews.append(review)
