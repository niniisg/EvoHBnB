import uuid

class Place_amenity:
    def __init__(self. name, description):
        self.name = name
        self.description = description
        self.placeamenity = []

    def add_place_amenity(self, place_amenity):
        if place_amenity not in self.placeamenity:
            self.placeamenity.append(place_amenity)

    def update_place_amenity(self, old_place_amenity, new_place_amenity):
        for idx, item in enumerate(self.placeamenity):
            if item == old_place_amenity:
                self.placeamenity[idx] = new_place_amenity
                return

    def description_place_amenity(self, place_amenity):
        for item in self.placeamenity:
            if item == place_amenity:
                return item.descrption
        return None

    def delete_place_amenity(self, place_amenity):
        if place_amenity in self.amenity:
            self.placeamenity.remove(place_amenity)
