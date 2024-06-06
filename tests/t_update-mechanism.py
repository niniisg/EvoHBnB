#!/usr/bin/python3

import unittest
from model.user import User

class TestUpdateMechanism(unittest.TestCase):
    def test_update_user_attributes(self):
        user = User(1, "user@test.com", "User")
        user.name = "Updated User"
        self.assertEqual(user.name, "Updated User")

if __name__ == '__main__':
    unittest.main()
