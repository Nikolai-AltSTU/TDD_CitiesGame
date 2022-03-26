import unittest
from CityGame import CityGameClass

class TestCityGame(unittest.TestCase):

    def test_createCityGame(self):
        self.assertIsNot(CityGameClass, 0, "Не удалось создать объект")

    def test_checkCities(self):
        cityGame = CityGameClass()
        self.assertIsNot(len(cityGame.cities), 0, "Пустой список городов")

    def test_checkIsCity(self):
        cityGame = CityGameClass()
        self.assertTrue(cityGame.checkIsCity("Барнаул"))
        self.assertTrue(cityGame.checkIsCity("Новосибирск"))
        self.assertFalse(cityGame.checkIsCity("Абракадабра"))
        self.assertFalse(cityGame.checkIsCity(""))
        self.assertTrue(cityGame.checkIsCity("белокуриха"))
        self.assertTrue(cityGame.checkIsCity("красноЯрск"))

    def test_repetition(self):
        cityGame = CityGameClass()
        self.assertFalse(cityGame.checkRepetition("Барнаул"))
        cityGame.addCity("Барнаул")
        self.assertFalse(cityGame.checkRepetition("Новосибирск"))
        cityGame.addCity("Новосибирск")
        self.assertTrue(cityGame.checkRepetition("Барнаул"))
        cityGame.addCity("Барнаул")


if __name__ == '__main__':
    unittest.main()