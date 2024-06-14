from .BaseModel import BaseModel
from model.city import City
from model.amenity import Amenity
from model.review import Review

class Place(BaseModel):
    def __init__(self, name, description, number_of_rooms, number_of_bathrooms, max_guests, price_per_night, latitude, longitude, city_id, amenity_ids):
        super().__init__()
        self.name = name
        self.host_id = None
        self.description = description
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = None
        self.amenity_ids = None
        
    
    def add_review(self, review_id):
        review_id = Review.self.id
        self.review_id = review_id
        

    
    def verify_name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self.name = name
        
    def assign_description(self, description):
        if description == "":
            raise ValueError("Description cannot be empty")
        self.description = description
        
    def verify_number_of_rooms(self, number_of_rooms):
        if isinstance(number_of_rooms, int):
            raise ValueError("Number of rooms cannot be empty")
        self.number_of_rooms = number_of_rooms
        
    def verify_number_of_bathrooms(self, number_of_bathrooms):
        if isinstance(number_of_bathrooms, int):
            raise ValueError("Number of bathrooms cannot be empty")
        self.number_of_bathrooms = number_of_bathrooms
        
    def verify_max_guests(self, max_guests):
        if isinstance (max_guests, int):
            raise ValueError("Max guests cannot be empty")
        self.max_guests = max_guests
        
    def verify_price_per_night(self, price_per_night):
        if isinstance(price_per_night):
            raise ValueError("Price per night cannot be empty")
        self.price_per_night = price_per_night
        
    def verify_latitude(self, latitude):
        if isinstance(latitude,  float):
            raise ValueError("Latitude cannot be empty")
        self.latitude = latitude
        
    def assign_longitude(self, longitude):
        if isinstance(longitude, float):
            raise ValueError("Longitude cannot be empty")
        self.longitude = longitude
        
    def assign_city_id(self, city_id):
        id = City.self.city_id 
        city_id = super().assign_id(id)
        if not city_id:
            raise ValueError("City ID is required") 
        self.city_id = city_id
        
    def assign_amenity_ids(self, amenity_ids):
        id = Amenity.self.amenity_id
        amenity_ids = super().assign_id(id)
        if not amenity_ids:
            raise ValueError("Amenity ID is required")
        self.amenity_ids = amenity_ids
        
    def add_place(self, user):
        if self.host_id == user.id:
            super().add(self)
            print("Place has been added")
        else:
            raise ValueError("You cannot add this place")
        
    
    def verify_delete_place(self):
        if self.host_id == self.id:
            super().delete(self)
            print("Place has been deleted")
        else:
            raise ValueError("You cannot delete this place")
                
    def update_place(self):
        if self.host_id == self.id:
            super().update(self)
            print("Place has been updated")
        else:
            raise ValueError("You cannot update this place")
    
    def modify_place(self):        
        if self.host_id == self.id:
            super().modify(self)
            print("Place has been modified")
        else:
            raise ValueError("You cannot modify this place")