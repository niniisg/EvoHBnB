#!/usr/bin/python3

import unittest
from model.user import User
from model.place import Place

class TestPlaceAttributeValidation(unittest.TestCase):
    def test_valid_coordinates(self):
        host = User(1, "host@test.com", "Host")
        place = Place(1, "Place", host)
        place.latitude = 40.7128
        place.longitude = -74.0060
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)

    def test_invalid_coordinates(self):
        host = User(1, "host@test.com", "Host")
        place = Place(1, "Place", host)
        with self.assertRaises(ValueError):
            place.latitude = 91
        with self.assertRaises(ValueError):
            place.longitude = -181

if __name__ == '__main__':
    unittest.main()
