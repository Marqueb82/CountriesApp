class Country:

    def __init__(self, country_name, population):
        self.countryName = country_name
        self.population = population

    def displayCountry(self):
        print("Country Name : ", self.countryName, ", Country Population: ", self.population)
