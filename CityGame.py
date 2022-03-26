
class CityGameClass:
    cities = []
    used_cities = []

    def __init__(self):
        citiesFile = open("cities.txt", encoding='utf-8')
        self.cities = []
        for i in citiesFile:
            if i[-1] == "\n":
                self.cities.append(i[:-1].lower())
            else:
                self.cities.append(i.lower())

    def checkIsCity(self, cityName):
        return cityName.lower() in self.cities

    def checkRepetition(self, cityName):
        return cityName.lower() in self.used_cities

    def addCity(self, cityName):
        self.used_cities.append(cityName.lower())

    def checkLinear(self, cityName):
        return self.used_cities[-1][-1] == cityName.lower()[0]







