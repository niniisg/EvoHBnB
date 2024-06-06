#!/usr/bin/python3

import unittest
from model.user import User
from model.place import Place

class TestHostAssignmentRules(unittest.TestCase):
    def test_assign_one_host(self):
        host = User(1, "host@test.com", "Host")
        place = Place(1, "Place", host)
        self.assertEqual(place.host, host)

    def test_reassign_host(self):
        host1 = User(1, "host1@test.com", "Host1")
        host2 = User(2, "host2@test.com", "Host2")
        place = Place(1, "Place", host1)
        place.host = host2
        self.assertEqual(place.host, host2)

if __name__ == '__main__':
    unittest.main()
