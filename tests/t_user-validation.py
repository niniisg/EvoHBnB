#!/usr/bin/python3

import unittest
from model.user import User

class TestUserCreationValidation(unittest.TestCase):
    def test_valid_user(self):
        user = User(1, "user@example.com", "User")
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.name, "User")

    def test_invalid_user(self):
        with self.assertRaises(ValueError):
            user = User(1, "invalid_email", "User")
