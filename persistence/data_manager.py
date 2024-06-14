from persistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}
        
    def save(self, object):
        self.storage[object.id] = object
          
    def get(self, object_id, object_type):
        return self.storage[object_id]

    def update(self, object):
        self.storage[object_id] = object
        
    def delete(self, entity_id, entity_type):
        if object in self.storage:
            del self.storage[object]
            
    def load(self, object):
        self.storage[object.id] = object