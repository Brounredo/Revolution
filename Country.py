import random

class CCountry:  # Класс государства
    # Постоянные данные
    name = ''  # Название государства
    capital = ''  # Столица

    # Переменные данные
    population = 1  # Население
    money = 1  # Деньги в казне
    army = 1  # Численность армии
    min_now = ["", "", "", "", ""]  # Текущий состав кабинета министров
    min_stats = [10, 10, 10, 10, 10]  # Уровень министров


    # Инициализация
    def __init__(self):
        self.population = random.randint(1000000, 1000000000)  # Население
        self.money = random.randint(1000000000, 5000000000)  # Деньги в казне
        self.army = random.randint(10000, 1000000)  # Численность армии
        for i in range(5):
            self.min_stats[i] = random.randint(1,10)

    def newcnt(self, name, capital):
        self.name = name
        self.capital = capital
