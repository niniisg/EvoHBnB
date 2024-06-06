#!/usr/bin/python3

import unittest
from model.user import User
from model.place import Place

class TestRetrieveAndUpdateAmenities(unittest.TestCase):
    def test_retrieve_amenities(self):
        host = User(1, "host@test.com", "Host")
        place = Place(1, "Place", host)
        place.add_amenity("Swimming Pool")
        place.add_amenity("Gym")
        self.assertIn("Swimming Pool", place.amenities)
        self.assertIn("Gym", place.amenities)

    def test_update_amenity(self):
        host = User(1, "host@test.com", "Host")
        place = Place(1, "Place", host)
        place.add_amenity("Swimming Pool")
        self.assertIn("Swimming Pool", place.amenities)
        place.update_amenity("Swimming Pool", "Indoor Pool")
        self.assertIn("Indoor Pool", place.amenities)
        self.assertNotIn("Swimming Pool", place.amenities)

if __name__ == '__main__':
    unittest.main()
