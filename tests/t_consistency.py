#!/usr/bin/python3

import unittest
from model.user import User

class TestConsistencyChecks(unittest.TestCase):
    def test_created_at_and_updated_at(self):
        user = User(1, "user@test.com", "User")
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

if __name__ == '__main__':
    unittest.main()
