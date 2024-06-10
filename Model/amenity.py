import uuid

class Amenity:
    def __init__(self, name, description):
        """
        Initialize a new Amenity instance.

        Args:
            name (str): The name of the amenity.
            description (str): The description of the amenity.
        """
        self.name = name
        self.description = description
        self.amenities = []

    def add_amenity(self, amenity):
        """
        Add an amenity to the list if it is not already present.

        Args:
            amenity (Amenity(: The amenity to add.
        """
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def update_amenity(self, old_amenity, new_amenity):
        """
        Update an existing amenity with a new amenity.
        Args:
            old_amenity (Amenity): The amenity to be replaced.
            new_amenity (Amenity): The new amenity to replace the old one.
        """
        for idx, item in enumerate(self.amenities):
            if item == old_amenity:
                self.amenities[idx] = new_amenity
                return

    def describe_amenity(self, amenity):
        """
        Get the description of a specific amenity.
        Args:
            amenity (Amenity): The amenity whose description is requested.

        Returns:
            str: The description of the amenity, or None if not found.
        """
        for item in self.amenities:
            if item == amenity:
                return item.description
        return None

    def delete_amenity(self, amenity):
        """
        Remove an amenity from the list if it is present.

        Args:
            amenity (Amenity): The amenith to remove.
        """
        if amenity in self.amenities:
            self.amenities.remove(amenity)
