#!/usr/bin/python3

import unittest
from model.place import Place
from model.user import User
from persistence.p_dao import PlaceDAO

class TestDeletingPlaces(unittest.TestCase):
    def test_delete_place(self):
        host = User(1, "host@test.com", "Host")
        place = Place(1, "Place", host)
        place_dao = PlaceDAO()
        place_dao.save_place(place)
        place_dao.delete_place(place)
        self.assertIsNone(place_dao.get_place_by_id(1))

if __name__ == '__main__':
    unittest.main()
