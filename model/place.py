#!/usr/bin/python3

class Place:
    def __init__(self, place_id, name, host):
        self.place_id = place_id
        self.name = name
        self.host = host
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def validate_one_host_per_place(self, place_dao):
        """
        Validates that only one host can be associated with each place.

        Args:
    place_dao (PlaceDAO): The data access object for place data.

        Returns:
            bool: True if the place can have the current host, False otherwise.
        """
        try:
            existing_place = place_dao.get_place_by_id(self.place_id)
            if existing_place and existing_place.host != self.host:
                return False
            return True
        except AttributeError:
            print("Error: The provided place_DAO object does not have a method 'get_place_by_id'.")
            return False

class PlaceDAO:
    def __init__(self):
        """Initializes a new Place_DAO instance with an empty list of places."""
        self .places = []

    def get_place_by_id(self, place_id):
        """
        Retrieves a place by it's unique identifier.

        Args:
            place_id (int): The unique identifier for the place.

        Returns:
            Place: The place with the specified place_id, or None if not found.
        """
        for place in self.places:
            if place.place_id == place_id:
                return place
        return None

    def add_place(self, place)"
        self.places.append(place)

# Creates an instance of PlaceDAO
place_dao = PlaceDAO()

# Creates a new Place instance
new_place = Place(place_id = 1, name = "", host = "") 
#Adds the new place to the place_dao
place_dao.add_place(new_place)

# Validates if the place has only one host
is_valid = new_place.validate_one_host_per_place(place_dao)

if is_valid:
    print("The host is valid for this place!")
else:
    print("This place already has a different host. Please choose another.")
