import unittest
from CityGame import CityGameClass

class TestNumpyRAID5(unittest.TestCase):

    def createCityGame(self):
        self.assertIsNot(CityGameClass, 0, "Не удалось создать объект")

    def loadCities(self):
        cityGame = CityGameClass
        self.assertIsNot(len(cityGame.cities), 0)
