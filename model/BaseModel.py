from flask import Flask
import uuid
import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.item():
                if key == "created_at" or key == "update_at":
                    self.__dict__[key] = datetime.strptime(value, dateformat)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
                self.id = str(uuid4)
                self.created_at = datetime.know
                self.update_at = self.created_at
                model.storage.new(self)
                model.storage.save()

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

class user(BaseModel):

    user = []

    def __init__(self, name, email, password):
        new_user = User(name, email, password):
        if new_user in User.user:
            raise ValueError("User is already exists")
        if email in User.used_emails:
            raise ValueError("email is already in used")
        self.__user__id = uuid.self.uuid4
        self.name = name
        self.__email = email
        User.used_emails.add(email)
        self.password = password
        self.reviews = []
