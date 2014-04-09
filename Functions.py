import Vars
import random
import sys
import Names
import Map

# Определения функций
def next_year():
    """Конец хода (1 ход = 1 год)."""
    Vars.year += 1  # Инкремент текущего года
    for e in Vars.players:  # Для всех игроков
        Vars.players[e].age += 1  # Инкремент возраста
    game_over()  # Проверка на конец игры
    for w in range(5):  # 5 раз
        Vars.MyCountry.min_now[w] = Names.random_name()  # присвоить министру с номером w случайное имя
    for q in range(5):  # 5 раз
        Vars.MyCountry.min_stats[q] = random.randint(1, 11)  # присвоить случайный уровень (от 1 до 10) министру q

def events():
    """Проверка событий."""
    pass

def game_over():
    if Vars.MyPlayer.age > 69:
        print("Вам уже 70 лет. Вы не способны управлять страной дальше.")
        input()
        sys.exit()
    elif Vars.MyPlayer.popular < 1:
        print("Ваша популярность на нуле. Никто вас больше не считает главой государства")
        input()
        sys.exit()
    elif Vars.MyCountry.money < 1:
        print("В казне больше нет денег. Страна развалилась.")
        input()
        sys.exit()
    elif Vars.MyPlayer.money < 1:
        print("У вас нет денег даже на кусок хлеба. Вы - никто.")
        input()
        sys.exit()
    elif Vars.MyPlayer.popular > 99:
        print("Вы успешно подавили Революцию! Поздравляю!")
        input()
        sys.exit()
    else:
        pass

def change_min():
    print("")
    print("Кого хотите заменить?")
    print("1. Премьер-министр")
    print("2. Министр внутренних дел")
    print("3. Министр финансов")
    print("4. Министр иностранных дел")
    print("5. Министр народного просвещения")
    cmd = input()
    print("Кого назначить (в формате Имя Фамилия)?")
    newname = input()
    Vars.MyCountry.min_now[int(cmd) - 1] = newname
    Vars.MyCountry.min_stats[int(cmd) - 1] = random.randint(1, 10)
    print("Готово!")

def save():
    game_data = {
		'players' : Vars.players,
        'countries' : Vars.countries
	}

def gen_gamemap():
    for q in range(100):
        Vars.gamemap.append(Map.CTile())
        Vars.gamemap[q].Country = random.choice(Vars.countries)
        if random.randint(0, 10) == 5:
            Vars.gamemap[q].Land = False
        Vars.gamemap[q].Char = Vars.gamemap[q].get_char(Vars.gamemap[q].Country)
        if Vars.gamemap[q].Country != Vars.VoidCountry:
            if Vars.is_lose == True:
                Vars.gamemap[q].Army = random.randint(100000, 100000000)
            else:
                Vars.gamemap[q].Army = random.randint(0, 1000)
    for i in range(random.randint(40, 60)):
        for j in range(len(Vars.gamemap) - 1):
            if Vars.countries.index(Vars.gamemap[j].Country) < Vars.countries.index(Vars.gamemap[j + 1].Country):
                x = Vars.gamemap[j]
                Vars.gamemap[j] = Vars.gamemap[j + 1]
                Vars.gamemap[j + 1] = x


def draw_gamemap():
    w, e, r, t, y, u, i, o, p, a = '', '', '', '', '', '', '', '', '', ''
    for q in range(10):
        w += Vars.gamemap[q].Char
        e += Vars.gamemap[q+10].Char
        r += Vars.gamemap[q+20].Char
        t += Vars.gamemap[q+30].Char
        y += Vars.gamemap[q+40].Char
        u += Vars.gamemap[q+50].Char
        i += Vars.gamemap[q+60].Char
        o += Vars.gamemap[q+70].Char
        p += Vars.gamemap[q+80].Char
        a += Vars.gamemap[q+90].Char
    print(w)
    print(e)
    print(r)
    print(t)
    print(y)
    print(u)
    print(i)
    print(o)
    print(p)
    print(a)
    print(' ')
    for qq in range(len(Vars.countries)):
        print(str(Map.CTile.get_char(Map.CTile(), Vars.countries[qq])) + ' - ' + Vars.countries[qq].name)


def xy_to_index(x, y):
    return (y*10-10)+(x-1)


def index_to_xy(index):
    x = -10 * index + 11
    y = ((-1 * x) + index + 11) / 10
    return [x, y]


def move(i1, i2, number):
    if can_move(i1, i2) == False:
        return
    if Vars.gamemap[i1].Army - number < 0:
        return
    Vars.gamemap[i2].Army += number
    Vars.gamemap[i1].Army -= number


def attack(i1, i2, number):
    if can_move(i1, i2) == False:
        return
    if Vars.gamemap[i1].Army - number < 0:
        return
    Vars.gamemap[i1].Army -= number
    Vars.gamemap[i2].Army -= number
    if Vars.gamemap[i2].Army < 0:
        Vars.gamemap[i2].Army = Vars.gamemap[i2].Army * (-1)
        Vars.gamemap[i2].Country = Vars.gamemap[i1].Country


def can_move(i1, i2):
    if ((i1 != i2+11)or(i1 != i2+10)or(i1 != i2+9)or(i1 != i2+1)or(i1 != i2)or(i1 != i2-1)or(i1 != i2-9)or
        (i1 != i2-10)or(i1 != i2-11)):
        return False
    else:
        return True


def real_age(age):
    if age < 12:
        return -1
    elif age > 60:
        return 1
    else:
        return 0
