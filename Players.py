import Biography
import random

class CPlayer:  # Класс игроков
    # Постоянные данные
    name = ''  # Имя игрока
    male = True  # Пол игрока (True - мужской, False - женский)
    country = ''  # Государство игрока
    biography = ''  # Биография игрока

    # Переменные данные
    place = ''  # Текущее местоположение игрока
    age = 1  # Возраст игрока

    # Технические данные
    platform = ''  # Платформа (Windows, Linux, Android, etc.)

    # Инициализация
    def __init__(self):
        pass


class CMyPlayer(CPlayer):  # Класс моего игрока
    # Постоянные данные
    def gen_bio(self):
        self.biography = Biography.bio(self.age)

    # Переменные данные
    money = 1000000  # Деньги игрока
    popular = 50  # Популярность игрока

    # Технические данные

    # Инициализация
    def __init__(self):
        self.money = random.randint(1000000, 1000000000)
        self.popular = random.randint(40, 60)
        pass
