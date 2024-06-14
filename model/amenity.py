from model.BaseModel import BaseModel


class Amenity(BaseModel):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.place_id = None
        
        
    def __dict__(self):
        return{
            'name': self.name,
            'description': self.description,
            'place id': self.place_id,
        }
    
        
    def add_amenity(self, name, description):
        if self.name:
            self.name = name
        if self.description:
            self.descripton = description
        super().save(self)
        super().__dict__(name='amenity name', description='amenity description')
        
            
    def update_amenity(self, name, description):
        if name:
            self.name = name
        if description:
            self.description = description
            
    def delete_amenity(self, amenity, cls='Amenity'):
        amenity = super().get_instances(cls)
        if isinstance(amenity, cls.__dict__):
            super().delete(self)