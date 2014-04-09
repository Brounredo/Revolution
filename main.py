# Инициализация
import Functions  # Определения функций
import Names  # Случайные имена
import Vars  # Переменные
import AllCountries  # Список реальных стран
import sys  # Системная библиотека
import random  # Генератор случайных чисел

# Интерактивная инициализация
Vars.is_lose = random.choice([True, False])  # Выиграет игрок или проиграет
print("")
print("Revolution v1.0")
print("-----")
print("Введите своё имя: ", end='')
Vars.MyPlayer.name = input()  # Имя игрока
print("Введите свой возраст (от 14 до 50 лет): ", end='')
age_temp = int(input())
if age_temp < 14:
    print("Маленький ещё страной управлять!")
    sys.exit()
elif age_temp > 50:
    print("Староват уже.")
    sys.exit()
Vars.MyPlayer.age = int(age_temp)  # Возраст игрока
Vars.MyCountry = random.choice(AllCountries.allcountries)  # Страна игрока
print("Ваша страна - ", Vars.MyCountry.name)
Vars.MyPlayer.place = Vars.MyCountry.capital  # Местоположение игрока
print("Введите количество ботов: ", end='')
bots = int(input())  # Количество ботов
for j in range(bots):  # Добавление ботов
    Vars.countries.append(random.choice(AllCountries.allcountries))
for q in range(5):  # "Созыв" министров
    Vars.MyCountry.min_now[q] = Names.random_name()
Functions.gen_gamemap()  # Генерация карты


# Цикл игры
while 1:
    # Вывод основной информации
    print("")
    print("Год:", Vars.year)
    print("Ваш возраст:", Vars.MyPlayer.age)
    print("Ваша популярность:", Vars.MyPlayer.popular)
    print("Денег в казне:", Vars.MyCountry.money, "руб.")
    print("Население страны:", Vars.MyCountry.population, "чел.")
    print("Личных денег:", Vars.MyPlayer.money, "руб.")
    print("Вы находитесь в:", Vars.MyPlayer.place)
    print("Новости:", Vars.news)
    print("-----")
    print("Для помощи напишите 'помощь' (без кавычек)")

    print("Введите команду: ", end='')
    # Ввод и обработка команды
    command = input()  # Воод команды
    if command == "конец хода":
        Functions.next_year()
    elif command == "министры":
        print("")
        print("Кабинет министров:")
        print("Премьер-министр:", Vars.MyCountry.min_now[0], "| Уровень:", Vars.MyCountry.min_stats[0])
        print("Министр внутренних дел:", Vars.MyCountry.min_now[1], "| Уровень:", Vars.MyCountry.min_stats[1])
        print("Министр финансов:", Vars.MyCountry.min_now[2], "| Уровень:", Vars.MyCountry.min_stats[2])
        print("Министр иностранных дел:", Vars.MyCountry.min_now[3], "| Уровень:", Vars.MyCountry.min_stats[3])
        print("Министр народного просвещения:", Vars.MyCountry.min_now[4], "| Уровень:", Vars.MyCountry.min_stats[4])
    elif command == "сменить министра":
        Functions.change_min()
    elif command == "выступить":
        for x in range(10):
            print(Names.random_phrase(), '.')
    elif command == "выход":
        sys.exit()
    elif command == "помощь":
        print('помощь, выход, конец хода, министры, сменить министра, выступить, тайл, карта')
    elif command == "карта":
        Functions.draw_gamemap()
    elif command == "тайл":
        print("Введите строку: ", end='')
        y = int(input())
        print("Введите столбец: ", end='')
        x = int(input())
        tile = Vars.gamemap[Functions.xy_to_index(x, y)]
        print("Страна: " + str(tile.Country.name))
        print("Защита: " + str(tile.Defence))
        print("Армия: " + str(tile.Army))
    elif command == "перебросить":
        print("Введите строку (откуда): ", end='')
        y1 = int(input())
        print("Введите столбец (откуда): ", end='')
        x1 = int(input())
        print("Введите строку (куда): ", end='')
        y2 = int(input())
        print("Введите столбец (куда) ", end='')
        x2 = int(input())
        print("Сколько войск перебросить: ", end='')
        n = int(input())
        Functions.move(Functions.xy_to_index(x1, y1), Functions.xy_to_index(x2, y2), n)
    elif command == "атаковать":
        print("Введите строку (откуда): ", end='')
        y1 = int(input())
        print("Введите столбец (откуда): ", end='')
        x1 = int(input())
        print("Введите строку (куда): ", end='')
        y2 = int(input())
        print("Введите столбец (куда) ", end='')
        x2 = int(input())
        print("Сколько человек послать: ", end='')
        Functions.attack(Functions.xy_to_index(x1, y1), Functions.xy_to_index(x2, y2), n)
    else:
        print("Нет такой команды!")
