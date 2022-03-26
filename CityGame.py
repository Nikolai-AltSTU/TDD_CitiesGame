
class CityGameClass:
    cities = []

    def __init__(self):
        citiesFile = open("cities.txt", encoding='utf-8')
        self.cities = []
        for i in citiesFile:
            if i[-1] == "\n":
                self.cities.append(i[:-1])
            else:
                self.cities.append(i)

    def checkIsCity(self, cityName):
        return cityName in self.cities









