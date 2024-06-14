from persistence.persistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}
        
    def save(self, object):
        self.storage[object.id] = object
          
    def get(self, object_id):
        return self.storage[object_id]

    def update(self, object):
        self.storage[object.id] = object
        
    def delete(self, object):
        if object in self.storage:
            del self.storage[object]
            
    def load(self, object):
        self.storage[object.id] = object