#!/usr/bin/python3

class User:
    def __init__(self, user_id, email, name):
        self.user_id = user_id
        self.email = email
        self.name = name

    def validate_unique_email(self, email, user_dao):
        existing_user = user_dao.get_user_by_email(email)
        if existing_user:
            return False
        return True
