class FilePersistenceManager(IPersistenceManager):

    def save(self, entity):
        # Implementation of saving the entity to a file
        print(f"Saving {entity}")

    def get(self, entity_id, entity_type):
        # Implementation of retrieving an entity from a file
        print(f"Getting {entity_type} with ID {entity_id}")

    def update(self, entity):
        # Implementation of updating the entity in a file
        print(f"Updating {entity}")

    def delete(self, entity_id, entity_type):
        # Implementation of deleting the entity from a file
        print(f"Deleting {entity_type} with ID {entity_id}")

# Example usage:
persistence_manager = FilePersistenceManager()
persistence_manager.save("SampleEntity")
persistence_manager.get(1, "SampleEntityType")
persistence_manager.update("SampleEntity")
persistence_manager.delete(1, "SampleEntityType")
