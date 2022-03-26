from CityGame import CityGameClass


def test_gameEmulation():
    cityGame = CityGameClass()
    assert cityGame.checkIsCity("Барнаул")
    assert not cityGame.checkRepetition("Барнаул")
    assert cityGame.checkLinear("Барнаул")
    cityGame.addCity("Барнаул")

    assert cityGame.checkIsCity("Новосибирск")
    assert not cityGame.checkRepetition("Новосибирск")
    assert not cityGame.checkLinear("Новосибирск")

    assert cityGame.checkIsCity("Липецк")
    assert not cityGame.checkRepetition("Липецк")
    assert cityGame.checkLinear("Липецк")
    cityGame.addCity("Липецк")

    assert cityGame.checkIsCity("Красноярск")
    assert not cityGame.checkRepetition("Красноярск")
    assert cityGame.checkLinear("Красноярск")
    cityGame.addCity("Красноярск")

    assert cityGame.checkIsCity("Красноярск")
    assert cityGame.checkRepetition("Красноярск")
    assert cityGame.checkLinear("Красноярск")
