import Vars  # Модуль переменных


class CTile:  # Класс тайла карты
	Land = True  # Земля или вода
	Country = Vars.VoidCountry  # Принадлежность государству
	City = ''  # Город, находящийся на тайле
	Defence = 1  # Защита тайла
	Army = 0  # Армия, находящаяся на тайле

	Char = '#'  # Отображаемый символ


	def get_char(self, country):
		if not self.Land:
			return '~'
		else:
			if country == Vars.VoidCountry:
				return '#'
			else:
				return str(Vars.countries.index(country))
				pass
