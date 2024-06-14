from flask import Flask
import uuid
import datetime
from storage import Storage

model = Storage()

class BaseModel:
    date_format = "%Y-%m-%d %H:%M:%S"

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.strptime(value, self.date_format)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            model.new(self)
            model.save()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

class User(BaseModel):
    users = []
    used_emails = set()

    def __init__(self, name, email, password):
        if email in User.used_emails:
            raise ValueError("Email  is already in use. Please provide different email.")
        super().__init__()
        self.name = name
        self.__email = email
        User.used_emails.add(email)
        self.password = password
        self.reviews = []
        User.users.append(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
