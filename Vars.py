# Подключаемые модули
import Players
import Country

# Объекты классов
MyPlayer = Players.CMyPlayer()  # Мой игрок
players = [MyPlayer]  # Массив всех игроков

MyCountry = Country.CCountry()  # Моя страна
VoidCountry = Country.CCountry()  # "Пустая" страна
VoidCountry.name = "Свободная территория"  # Название "пустой" страны
countries = [MyCountry, VoidCountry]  # Массив всех стран

# Глобальные переменные
year = 1700  # Текущий год
news = ''  # Текущие новости

gamemap = []  # Карта

is_lose = False  # True - игрок проиграет, False - игрок может выиграть

# Технические переменные
is_sync = False  # Заданы ли имя, возраст, страна игрока
