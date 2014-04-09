# Инициализация
from tkinter import *  # Библиртека tkinter
from tkinter.messagebox import showinfo  # Всплывающие окна
import Functions  # Определения функций
import Names  # Случайные имена
import Vars  # Переменные
import AllCountries  # Список реальных стран
import sys  # Системная библиотека
import random  # Генератор случайных чисел

# Константы
def_font = 'Arial 14'  # Шрифт по умолчанию

# Основные команды и параметры
root = Tk()  # Создание окна
root.title('Revolution')  # Название окна
#root.geometry("1024x768")  # Размер окна (по умолчанию - "800x600")
#root.resizable(False, False)  # Можно ли изменить размер

# Функции
def start_game():
    if Functions.real_age(int(AgeEnt.get())) == -1:
        showinfo(title='Ошибка!', message='Ещё маленький страной управлять!')
        root.quit()
    elif Functions.real_age(int(AgeEnt.get())) == 1:
        showinfo(title='Ошибка!', message='Стар уже страной управлять!')
        root.quit()
    else:
        Vars.MyPlayer.age = int(AgeEnt.get())
    Vars.MyPlayer.name = NameEnt.get()

# Текст
Label(root, text='Ваше имя: ').grid(row=0, column=0)
Label(root, text='Ваш возраст: ').grid(row=1, column=0)

# Кнопки
Button(root, text="Старт игры", command=start_game).grid(row=3, column=0)

# Поля ввода текста
NameEnt = Entry(root)  # Поле имени
NameEnt.grid(row=0, column=1)
AgeEnt = Entry(root)  # Поле возраста
AgeEnt.grid(row=1, column=1)

root.mainloop()  # Главный цикл
