#!/usr/bin/python3

import unittest
from model.user import User
from model.place import Place
from persistence.u_dao import UserDAO

class TestBusinessRuleEnforcement(unittest.TestCase):
    def test_one_host_per_place(self):
        host1 = User(1, "host1@test.com", "Host1")
        host2 = User(2, "host2@test.com", "Host2")
        place = Place(1, "Place", host1)
        with self.assertRaises(ValueError):
            place.host = host2

    def test_user_uniqueness(self):
        user1 = User(1, "user1@test.com", "User1")
        user2 = User(2, "user1@test.com", "User2")
        user_dao = UserDAO()
        user_dao.save_user(user1)
        with self.assertRaises(ValueError):
            user_dao.save_user(user2)

if __name__ == '__main__':
    unittest.main()
