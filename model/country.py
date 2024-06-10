import uuid

class Country:
    def __init__ (self, country_name, area_code):
        self.country_name = country_name
        self.area_code = area_code
        
        def country_name(self, country_name):
            if country_name == "":
                return "Country name cannot be empty"
            self.country_name.append(country_name)
            return self.country_name
        
        def area_code(self, area_code):
            if area_code == "":
                return "Area code cannot be empty"
            self.area_code.append(area_code)
            return self.area_code
        
