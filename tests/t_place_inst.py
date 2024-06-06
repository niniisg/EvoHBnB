#!/usr/bin/python3

import unittest
from model.place import Place
from model.user import User

class TestPlaceInstantiation(unittest.TestCase):
    def test_valid_place(self):
        host = User(1, "host@example.com", "Host")
        place = Place(1, "Place", host)
        self.assertEqual(place.name, "Place")
        self.assertEqual(place.host, host)

    def test_invalid_place(self):
        with self.assertRaises(ValueError):
            place = Place(1, "", None)

if __name__ == '__main__':
    unittest.main()
