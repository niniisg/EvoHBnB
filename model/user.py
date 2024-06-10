#!/usr/bin/python3

class User:
    def __init__(self, user_id, email, name):
        self.user_id = user_id
        self.email = email
        self.name = name

    def validate_unique_email(self, email, user_dao):
        existing_user = user_dao.get_user_by_email(email)
        return existing_user is None

class UserDAO:
    def __init__(self):
        # User storage
        self.users = []

    def get_user_by_email(self, email):
        # Database lookup
        for user in self.users:
            if user.email == email:
                return user
        return None

    def add_user(self, user):
        self.users.appen(user)

# Creates an instance of UserDAO
user_dao = UserDAO()

# Create a new User instance
new_user = User(user_id = 1, email = "", name = "")

# Add the new user to the user_dao (for testing purposes)
user_dao.add_user(new_user)

#Validate if the email is unique
is_unique = new_user.validate_unique_email("", user_dao)

if is_unique:
    print("Email is available.")
else:
    print("Email already in use. Please use a different one.")
