import uuid
from review import Review
from place import Place
from country import Country, city
from amenity import Amenity


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
        self.first_name = new_name
        self.last_name = new_name
        
    
    
    def create_at(self, user):
        self.users.append(user)
        return self.users
    
    def update_user(self, user):
        self.users.append(user)
        return self.users
        
    def modify_user(self, user):
        self.users.append(user)
        return self.users
        
    def delete_user(self, user):
        self.users.remove(user)
        return self
        
    def email_user(self, user):
        self.users.append(user)
        return self.users
    
    
    if not self.email:
        raise ValueError("Email is required")

    def validate_unique_email(self, email, user_dao):
        existing_user = user_dao.get_user_by_email(email)
        if existing_user:
            return False
        return True
