import uuid
from model.review import Review
from model.place import Place
from model.country import Country
from model.city import City
from model.amenity import Amenity
import datetime

class User:
    used_emails = set()
    
    users = []

    def __init__(self, first_name, last_name,  email, password):
        self.__user__id = uuid.self.uuid4
        self.first_name = first_name
        self.last_name = last_name
        self.__email = email
        User.used_emails.add(email)
        self.password = password
        self.reviews = []
        
        
    def __dict__(self):
        return {
            "id": self.__user__id,
            "name": self.name,
            "email": self.__email,
            "password": self.password,
        }
    
    def new_name(self, first_name, last_name):
    
        if first_name == self.first_name and last_name == self.last_name:
            raise ValueError("The new name is the same as the existing name")
    
        if first_name == "":
            raise ValueError("First name cannot be empty")
        self.first_name = first_name
    
        if last_name == "":
            raise ValueError("Last name cannot be empty")
        self.last_name = last_name

    
    def validate_create_at(self, user):
        if user.create_at is None:
            raise ValueError("Please enter a valid date")
    
    def update_user(self, user):
        if user.first_name:
            self.first_name = user.first_name
        if user.last_name:
            self.last_name = user.last_name
    
    def modify_user(self, email=None, password=None, first_name=None, last_name=None):
        if email and email != self.email and email in User.users:
            raise ValueError("User with email {} already exists".format(email))
        if email:
           del User.used_emails[self.email] 
           self.email = email
           User.used_emails[self.email] = self
        if password:
            self.password = password
        if first_name:
            self.first_name = first_name # Update the first name
        if last_name:
            self.last_name = last_name # Update the last name
        self.updated_at = datetime.now()

   
    
    def delete_user(self, user):
        self.ussers.remove(user)
        return self.users

    def email_user(self, user):
        if not self.email:
            raise ValueError("Email is required")
        self.users.append(user)
        return self.users

    def validate_unique_email(self, email, user_dao):
        existing_user = user_dao.get_user_by_email(email)
        if existing_user:
            return False
        return True
