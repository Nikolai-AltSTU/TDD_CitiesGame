from CityGame import CityGameClass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Привет, {name}!')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('игрок')
    print("Будем играть в города России!")
    cityGame = CityGameClass()
    key = '1'
    city = ''
    while key != '0':

        inp = input("Введите название города: ").split()
        while len(inp) == 0:
            inp = input().split()
        city = inp[0]
        if not cityGame.checkIsCity(city):
            print("Город с таким названием не найден!")
            continue

        if cityGame.checkRepetition(city):
            print(f"{city} уже был назван!")
            continue

        if not cityGame.checkLinear(city):
            print(f"{city} нельзя назвать после {cityGame.used_cities[-1]}!")
            print("Нужно называть город на букву, на которую закончился предыдущий город.")
            continue

        cityGame.addCity(city)

        print("Город назван правильно!")
        print("Чтобы выйти из игры, введите 0.")

        inp = input("Чтобы продолжить игру, нажмите любую другую клавишу.").split()
        if len(inp) > 0:
            key = inp[0]
