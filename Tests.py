import unittest
from CityGame import CityGameClass

class TestCityGame(unittest.TestCase):

    def test_createCityGame(self):
        self.assertIsNot(CityGameClass, 0, "Не удалось создать объект")

    def test_checkCities(self):
        cityGame = CityGameClass()
        self.assertIsNot(len(cityGame.cities), 0, "Пустой список городов")

    def test_loadCities(self):
        cityGame = CityGameClass()
        self.assertTrue("Барнаул" in cityGame.cities, "Нет столицы мира в списке городов")

    def test_checkIsCity(self):
        self.assertTrue(CityGameClass().checkIsCity("Барнаул"))
        self.assertTrue(CityGameClass().checkIsCity("Новосибирск"))
        self.assertFalse(CityGameClass().checkIsCity("Абракадабра"))
        self.assertFalse(CityGameClass().checkIsCity(""))

if __name__ == '__main__':
    unittest.main()