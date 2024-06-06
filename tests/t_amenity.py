#!/usr/bin/python3

import unittest
from model.user import User
from model.place import Place

class TestAmenityAddition(unittest.TestCase):
    def test_add_amenities_to_place(self):
        host = User(1, "host@test.com", "Host")
        place = Place(1, "Place", host)
        place.add_amenity("Swimming Pool")
        place.add_amenity("Gym")
        self.assertEqual(len(place.amenities), 2)
        place.add_amenity("Swimming Pool")
        self.assertEqual(len(place.amenities), 2)  # Duplicates are not added

if __name__ == '__main__':
    unittest.main()
