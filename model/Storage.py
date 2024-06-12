import datetime

class Storage:
    def __init__(self):
        self.objects = {}

    def new(self, obj):
        """Adds new object to storage."""
        key = obj.__class__.__name__ + "." + obj.id
        self.objects[key] = obj

    def save(self):
        """Saves the current state of the storage."""
        pass

    def get(self, key):
        """Retrieves an object from storage."""
        return self.objects.get(key)

    def delete(self, key):
        if key in self.objects:
            del.self.objects[key]
