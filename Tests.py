import unittest
from CityGame import CityGameClass

class TestCityGame(unittest.TestCase):

    def test_createCityGame(self):
        self.assertIsNot(CityGameClass, 0, "Не удалось создать объект")

    def test_checkCities(self):
        cityGame = CityGameClass()
        self.assertIsNot(len(cityGame.cities), 0, "Пустой список городов")

    def test_checkIsCity(self):
        self.assertTrue(CityGameClass().checkIsCity("Барнаул"))
        self.assertTrue(CityGameClass().checkIsCity("Новосибирск"))
        self.assertFalse(CityGameClass().checkIsCity("Абракадабра"))
        self.assertFalse(CityGameClass().checkIsCity(""))
        self.assertTrue(CityGameClass().checkIsCity("белокуриха"))
        self.assertTrue(CityGameClass().checkIsCity("красноЯрск"))

    def test_emulateGame(self):
        cityGame = CityGameClass()
        self.assertFalse(cityGame.checkRepetion("Барнаул"))
        self.assertFalse(cityGame.checkRepetion("Новосибирск"))


if __name__ == '__main__':
    unittest.main()