from Validator import Validator
from Country import Country

china = Country("China", 1415045928)
egypt = Country("Egypt", 99375741)
italy = Country("Italy", 59290969)
turkey = Country("Turkey", 81916871)
russia = Country("Russia", 144500000)
india = Country("India", 1339000000)
canada = Country("Canada", 36710000)
australia = Country("Australia", 24600000)
germany = Country("Germany", 82790000)

countries = [china, egypt, italy, turkey, russia, india, canada, australia, germany]


def printCountries():
    for country in countries:
        country.displayCountry()


def addCountry():
    name = Validator.inputCountry("Enter country name: ")
    population = Validator.inputPopulation("enter country population: ")
    country = Country(name, population)
    countries.append(country)


def byCountry():
    countries.sort(key=lambda country: country.countryName)
    printCountries()


def byPopulation():
    countries.sort(key=lambda country: country.population, reverse=True)
    printCountries()


intro_str = """\nThis is a simple population application.
You will be able to see a list of countries alphabetically or 
by population and also add to the list of companies\n"""

menu_str = """\n1 - See the list of countries
2 - Add a country
3 - View alphabetically
4 - View by population
5 - Exit\n"""

print(intro_str)

var = 0;
while var != 5:
    print(menu_str)


    def one():
        printCountries()


    def two():
        addCountry()


    def three():
        byCountry()


    def four():
        byPopulation()


    def five():
        print("Thank you, goodbye")
        raise SystemExit


    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five
    }


    def user_choice(arg1):
        func = switcher.get(arg1)
        return func()


    choice = Validator.inputNumber("Selection: ")

    user_choice(choice)