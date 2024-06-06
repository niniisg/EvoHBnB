#!/usr/bin/python3

import unittest
from model.user import User
from model.place import Place
from model.review import Review


class TestRelationshipIntegrity(unittest.Testcase):
    def test_places_to_host_users(self):
        host = User(1, "host@test.com", "Host")
        place = Place(1, "Place", host)
        self.assertEqual(place.host, host)

    def test_reviews_to_places_and_users(self):
        user = User(1, "user@test.com", "User")
        place = Place(1, "Place", user)
        review = Review(1, place, user, 5, "Great place!")
        self.assertEqual(review.user, user)
        self.assertEqual(review.place, place)

if __name__ == '__main__':
    unittest.main()
