#!/usr/bin/python3

class UserDAO:
    def __init__(self):
        self.users = []

    def save_user(self, user):
        self.users.append(user)

    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None
