import pycountry


class Country:
    def __init__ (self, country_name, country_code):
        self.country_name = country_name
        self.country_code = country_code

    def country_name(self, country_name):
        if country_name is None:
            raise ValueError("Please enter a Country.")
        self.country_name = country_name
        print(f'The name of the country is {self.country_name}')

    def set_country_code(self, country_code):
        if len(country_code) != 2 or not country_code.isalpha():
            raise ValueError("Invalid country code. It must be a 2-letter alpha code according to ISO 3166-1 alpha-2.")

        try:
            pycountry.countries.get(alpha_2=country_code.upper())
        except KeyError:
            raise ValueError("Invalid country code. It must be a valid ISO 3166-1 alpha-2 country code.")

        self.country_code = country_code.upper()
        print(f'The country code is {self.country_code}')        
