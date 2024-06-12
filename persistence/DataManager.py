import json
from typing import Any, Dict
from persistance.IPersistanceManager import IPersistanceManager
from model.BaseModel import BaseModel


class DataManager(IPersistanceManager):
    def __init__(self):
        self.storage: Dict[str, Dict[Any, BaseModel]] = {}
        self.load_countries()

    def load_countries(self) -> None:
        """Load countries from a JSON file into the storage."""
        try:
            with open('countries.json', 'r') as f:
                countries = json.load(f)
            self.storage[Country'] = {country['code']: country for country in countries}
        except FileNotFoundError:
            self.storage['Country'] = {}

    def save(self, entity: BaseModel) -> None:
        """Saves an entity to the storage."""
        if not isinstance(entity, BaseModel):
            raise TypeError("Entity must be an instance of the BaseModel")
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity
        entity.save()

    def get(self, entity_id: Any, entity_type: str) -> BaseModel:
        """Retrieves an entity from the storage by ID and Type."""
        if entity_type in self.storage:
            return self.storage[entity_type].get(entity_id)
        return None

    def update(self, entity: BaseModel) -> None:
        """Updates an existing entity in the storage."""
        if not isinstance(entity, BaseModel):
            raise TypeError("Entity must be an instance of the BaseModel")
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity
            entity.save()
        else:
            raise ValueError("Entity not found in storage")

    def delete(self, entity_id: Any, entity_type: str) -> None:
        """Deletes an entity from the storage."""
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
        else:
            raise ValueError("Entity not found in storage")
