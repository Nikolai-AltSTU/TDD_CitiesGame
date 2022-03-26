
class CityGameClass:
    cities = []

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

    def checkRepetion(self, cityName):
        return False;








