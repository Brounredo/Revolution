import random

def random_name(arg = "male"):
    names_male = ["Абрам", "Аввакум", "Авдей", "Аверьян", "Авксентий", "Агап", "Агафон", "Аггей", "Адам", "Адриан", "Акакий", "Аким", "Александр", "Алексей", "Альберт", "Альфред", "Амвросий", "Ананий", "Анатолий", "Андрей", "Аникей", "Антип", "Антон", "Аполлинарий", "Аполлон", "Ардалион", "Аристарх", "Аркадий", "Арнольд", "Арсений", "Артемий", "Артём", "Артур", "Архип", "Аскольд", "Афанасий", "Афиноген", "Африкан", "Бенедикт", "Богдан", "Болеслав", "Борис", "Боян", "Бронислав", "Будимир", "Вавила", "Вадим", "Валентин", "Валерий", "Валерьян", "Валериан", "Варлаам", "Варлам", "Василий", "Венедикт", "Вениамин", "Викентий", "Виктор", "Виссарион", "Виталий", "Владилен", "Владимир", "Владислав", "Владлен", "Влас", "Всеволод", "Вячеслав", "Гавриил", "Гаврила", "Галактион", "Гедеон", "Геннадий", "Генрих", "Георгий", "Герасим", "Герман", "Глеб", "Гордей", "Григорий", "Гурий", "Давид", "Даниил", "Дементий", "Демид", "Демьян", "Денис", "Дмитрий", "Добрыня", "Доминик", "Донат", "Дормидонт", "Дорофей", "Досифей", "Евгений", "Евграф", "Евдоким", "Евлампий", "Евсей", "Евстафий", "Евстигней", "Евстрат", "Егор", "Елизар", "Елисей", "Емельян", "Епифан", "Еремей", "Ермил", "Ермолай", "Ерофей", "Ефим", "Ефрем", "Захар", "Зиновий", "Зосима", "Иакинф", "Иван", "Игнатий", "Игорь", "Иероним", "Измаил", "Изот", "Иларион", "Илья", "Иннокентий", "Йов", "Иона", "Иосиф", "Осиф", "Ипполит", "Иринарх", "Ириней", "Исаак", "Исай", "Исидор", "Казимир", "Калиник", "Каллистрат", "Капитон", "Касьян", "Ким", "Кир", "Кириак", "Кирилл", "Климент", "Кондрат", "Константин", "Корнелий", "Корнил", "Ксенофонт", "Кузьма", "Лаврентий", "Лазарь", "Лев", "Леонард", "Леонид", "Леонтий", "Леопольд", "Лука", "Лукьян", "Любим", "Любомир", "Маврикий", "Макар", "Максим", "Максимилиан", "Марат", "Марк", "Маркел", "Мартын", "Мартьян", "Матвей", "Мирон", "Мисаил", "Митрофан", "Михаил", "Михей", "Модест", "Моисей", "Мстислав", "Назар", "Наркис", "Натан", "Наум", "Нестор", "Никандр", "Никанор", "Никита", "Никифор", "Никодим", "Николай", "Никон", "Нифонт", "Олег", "Олимпий", "Онисим", "Анисим", "Онуфрий", "Орест", "Остап", "Павел", "Павлин", "Панкрат", "Панкратий", "Пантелей", "Пантелеймон", "Парамон", "Парфён", "Патрикей", "Пафнутий", "Пахом", "Пётр", "Пимен", "Платон", "Полиект", "Поликарп", "Порфирий", "Потап", "Пров", "Прокл", "Прокофий", "Прокопий", "Прохор", "Радий", "Рафаил", "Ричард", "Роберт", "Родион", "Роман", "Ростислав", "Рубен", "Рудольф", "Руслан", "Савва", "Савватий", "Савелий", "Салтан", "Самсон", "Светозар", "Святослав", "Севостьян", "Селиван", "Семён", "Серафим", "Сергей", "Сигизмунд", "Сидор", "Силантий", "Сильвестр", "Симон", "Созон", "Сократ", "Соломон", "Софрон", "Спиридон", "Станислав", "Степан", "Сысой", "Тарас", "Терентий", "Тимофей", "Тимур", "Тихон", "Трифон", "Трофим", "Ульян", "Устин", "Фадей", "Фалалей", "Фёдор", "Федот", "Феликс", "Феоктист", "Феофан", "Феофилакт", "Ферапонт", "Филарет", "Филимон", "Филипп", "Филофей", "Фока", "Фома", "Фотий", "Фрол", "Харитон", "Харлампий", "Христофор", "Эдуард", "Эмиль", "Эммануил", "Эраст", "Эрнест", "Юлиан", "Юлий", "Юрий", "Яков", "Ярослав"]
    surnames_male = ["Смирнов", "Иванов", "Кузнецов", "Соколов", "Попов", "Лебедев", "Козлов", "Новиков", "Морозов", "Петров", "Волков", "Соловьёв", "Васильцев", "Зайцев", "Павлов", "Семёнов", "Голубев", "Виноградов", "Богданов", "Воробьёв", "Фёдоров", "Михайлов", "Беляев", "Тарасов", "Белов", "Комаров", "Орлов", "Киселёв", "Макаров", "Андреев", "Ковалёв", "Ильин", "Гусев", "Титов", "Кузьмин", "Кудрявцев", "Баранов", "Куликов", "Алексеев", "Степанов", "Яковлев", "Сорокин", "Сергеев", "Романов", "Захаров", "Борисов", "Королёв", "Герасимов", "Пономарёв", "Григорьев", "Лазарев", "Медведев", "Ершов", "Никитин", "Соболев", "Рябов", "Поляков", "Цветков", "Данилов", "Жуков", "Фролов", "Журавлёв", "Николаев", "Крылов", "Максимов", "Сидоров", "Осипов", "Белоусов", "Федотов", "Дорофеев", "Егоров", "Матвеев", "Бобров", "Дмитриев", "Калинин", "Анисимов", "Петухов", "Антонов", "Тимофеев", "Никифоров", "Веселов", "Филиппов", "Марков", "Большаков", "Суханов", "Миронов", "Ширяев", "Александров", "Коновалов", "Шестаков", "Казаков", "Ефимов", "Денисов", "Громов", "Фомин", "Давыдов", "Мельников", "Щербаков", "Блинов", "Колесников", "Карпов", "Афанасьев", "Власов", "Маслов", "Исаков", "Тихонов", "Аксёнов", "Гаврилов", "Родионов", "Котов", "Горбунов", "Кудряшов", "Быков", "Зуев", "Третьяков", "Савельев", "Панов", "Рыбаков", "Суворов", "Абрамов", "Воронов", "Мухин", "Архипов", "Трофимов", "Мартынов", "Емельянов", "Горшков", "Чернов", "Овчинников", "Селезнёв", "Панфилов", "Копылов", "Михеев", "Галкин", "Назаров", "Лобанов", "Лукин", "Беляков", "Потапов", "Некрасов", "Хохлов", "Жданов", "Наумов", "Шилов", "Воронцов", "Ермаков", "Дроздов", "Игнатьев", "Савин", "Логинов", "Сафонов", "Капустин", "Кириллов", "Моисеев", "Елисеев", "Кошелев", "Костин", "Горбачёв", "Орехов", "Ефремов", "Исаев", "Евдокимов", "Калашников", "Кабанов", "Носков", "Юдин", "Кулагин", "Лапин", "Прохоров", "Нестеров", "Харитонов", "Агафонов", "Муравьёв", "Ларионов", "Федосеев", "Зимин", "Пахомов", "Шубин", "Игнатов", "Филатов", "Крюков", "Рогов", "Кулаков", "Терентьев", "Молчанов", "Владимиров", "Артемьев", "Гурьев", "Зиновьев", "Гришин", "Кононов", "Дементьев", "Ситников", "Симонов", "Мишин", "Фадеев", "Комиссаров", "Мамонтов", "Носов", "Гуляев", "Шаров", "Устинов", "Вишняков", "Евсеев", "Лаврентьев", "Брагин", "Константинов", "Корнилов", "Авдеев", "Зыков", "Бирюков", "Шарапов", "Никонов", "Щукин", "Дьячков", "Одинцов", "Сазонов", "Якушев", "Красильников", "Гордеев", "Самойлов", "Князев", "Беспалов", "Уваров", "Шашков", "Бобылёв", "Доронин", "Белозёров", "Рожков", "Самсонов", "Мясников", "Лихачёв", "Буров", "Сысоев", "Фомичев", "Русаков", "Стрелков", "Гущин", "Тетерин", "Колобов", "Субботин", "Фокин", "Блохин", "Селиверстов", "Пестов", "Кондратьев", "Силин", "Меркушев", "Лыткин", "Туров"]

    names_female = ["Августа", "Аврора", "Агафья", "Аглаида", "Аглая", "Агнесса", "Агния", "Аграфена", "Агриппина", "Ада", "Аделаида", "Аида", "Акулина", "Алевтина", "Александра", "Алина", "Алиса", "Алла", "Анастасия", "Ангелина", "Анжелика", "Анисья", "Анна", "Антонида", "Антонина", "Анфиса", "Ариадна", "Беатриса", "Белла", "Берта", "Бронислава", "Валентина", "Валерия", "Варвара", "Василиса", "Васса", "Вера", "Вероника", "Виктория", "Вилена", "Виргиния", "Виринея", "Владилена", "Владлена", "Галина", "Генриетта", "Гертруда", "Глафира", "Гликерия", "Дарья", "Диана", "Дина", "Домна", "Доротея", "Ева" ,"Евгения", "Евдокия", "Евлампия", "Евпраксия", "Евфимия", "Екатерина", "Елена", "Елизавета", "Ефросинья", "Жанна", "Жозефина", "Зинаида", "Зиновия", "Злата", "Зоя", "Изабелла", "Изольда", "Инесса", "Инна", "Ираида", "Ирина", "Ирма", "Ия", "Калерия", "Капитолина", "Каролина", "Кира", "Клавдия", "Клара", "Клариса", "Клеопатра", "Конкордия", "Констанция", "Ксения", "Лада", "Лариса", "Лаура", "Леокадия", "Лиана", "Лидия", "Лилия", "Лия", "Луиза", "Лукерья", "Любовь", "Людмила", "Мавра", "Магдалина", "Майя", "Мальвина", "Манефа", "Маргарита", "Марианна", "Марина", "Мария", "Марта", "Марфа", "Матрёна", "Меланья", "Мелитриса", "Милица", "Муза", "Надежда", "Наина", "Наталья", "Нелли", "Неонила", "Нина", "Нинель", "Нонна", "Оксана", "Октябрина", "Олимпиада", "Олимпия", "Ольга", "Павла", "Пелагея", "Полина", "Прасковья", "Пульхерия", "Раиса", "Рахиль", "Ревекка", "Регина", "Рената", "Римма", "Рогнеда", "Роза", "Розалия", "Руфина", "Руфь", "Сабина", "Сарра", "Светлана", "Серафима", "Софья", "Стелла", "Степанида", "Сусанна", "Таисия", "Тамара", "Татьяна", "Тереза", "Улита", "Ульяна", "Устинья", "Фаина", "Феврония", "Федора", "Федосья", "Фёкла", "Фелицата", "Феония", "Флора", "Христина", "Цецилия", "Шарлотта", "Эвелина", "Элеонора", "Элла", "Эльвира", "Эльза", "Эмилия", "Эмма", "Эсфирь", "Юлия", "Юнона", "Ядвига"]
    surnames_female = ["Смирнова", "Иванова", "Кузнецова", "Соколова", "Попова", "Лебедева", "Козлова", "Новикова", "Морозова", "Петрова", "Волкова", "Соловьёва", "Васильцева", "Зайцева", "Павлова", "Семёнова", "Голубева", "Виноградова", "Богданова", "Воробьёва", "Фёдорова", "Михайлова", "Беляева", "Тарасова", "Белова", "Комарова", "Орлова", "Киселёва", "Макарова", "Андреева", "Ковалёва", "Ильина", "Гусева", "Титова", "Кузьмина", "Кудрявцева", "Баранова", "Куликова", "Алексеева", "Степанова", "Яковлева", "Сорокина", "Сергеева", "Романова", "Захарова", "Борисова", "Королёва", "Герасимова", "Пономарёва", "Григорьева", "Лазарева", "Медведева", "Ершоав", "Никитин", "Соболев", "Рябов", "Поляков", "Цветков", "Данилов", "Жуков", "Фролов", "Журавлёв", "Николаев", "Крылов", "Максимов", "Сидоров", "Осипов", "Белоусов", "Федотов", "Дорофеев", "Егорова", "Матвеева", "Боброва", "Дмитриева", "Калинина", "Анисимова", "Петухова", "Антонова", "Тимофеева", "Никифорова", "Веселова", "Филиппова", "Маркова", "Большакова", "Суханова", "Миронова", "Ширяева", "Александрова", "Коновалова", "Шестакова", "Казакова", "Ефимова", "Денисова", "Громова", "Фомина", "Давыдова", "Мельникова", "Щербакова", "Блинова", "Колесникова", "Карпова", "Афанасьева", "Власова", "Маслова", "Исакова", "Тихонова", "Аксёнова", "Гаврилова", "Родионова", "Котова", "Горбунова", "Кудряшова", "Быкова", "Зуева", "Третьякова", "Савельева", "Панова", "Рыбакова", "Суворова", "Абрамова", "Воронова", "Мухина", "Архипова", "Трофимова", "Мартынова", "Емельянова", "Горшкова", "Чернова", "Овчинникова", "Селезнёва", "Панфилова", "Копылова", "Михеева", "Галкина", "Назарова", "Лобанова", "Лукина", "Белякова", "Потапова", "Некрасова", "Хохлова", "Жданова", "Наумова", "Шилова", "Воронцова", "Ермакова", "Дроздова", "Игнатьева", "Савина", "Логинова", "Сафонова", "Капустина", "Кириллова", "Моисеева", "Елисеева", "Кошелева", "Костинаа", "Горбачёва", "Орехова", "Ефремова", "Исаева", "Евдокимова", "Калашникова", "Кабанова", "Носкова", "Юдина", "Кулагина", "Лапина", "Прохорова", "Нестерова", "Харитонова", "Агафонова", "Муравьёва", "Ларионова", "Федосеева", "Зимина", "Пахомова", "Шубина", "Игнатова", "Филатова", "Крюкова", "Рогова", "Кулакова", "Терентьева", "Молчанова", "Владимирова", "Артемьева", "Гурьева", "Зиновьева", "Гришина", "Кононова", "Дементьева", "Ситникова", "Симонова", "Мишина", "Фадеева", "Комиссарова", "Мамонтова", "Носова", "Гуляево", "Шарова", "Устинова", "Вишнякова", "Евсеева", "Лаврентьева", "Брагина", "Константинова", "Корнилова", "Авдеева", "Зыкова", "Бирюкова", "Шарапова", "Никонова", "Щукина", "Дьячкова", "Одинцова", "Сазонова", "Якушева", "Красильникова", "Гордеева", "Самойлова", "Князева", "Беспалова", "Уварова", "Шашкова", "Бобылёва", "Доронина", "Белозёрова", "Рожкова", "Самсонова", "Мясникова", "Лихачёва", "Бурова", "Сысоева", "Фомичева", "Русакова", "Стрелкова", "Гущина", "Тетерина", "Колобова", "Субботина", "Фокина", "Блохина", "Селиверстова", "Пестова", "Кондратьева", "Силина", "Меркушева", "Лыткина", "Турова"]

    if arg == "male":
        ret = names_male[random.randint(0, len(names_male) - 1)] + ' ' + surnames_male[random.randint(0, len(surnames_male) - 1)]
    else:
        ret = names_female[random.randint(0, len(names_female) - 1)] + ' ' + surnames_female[random.randint(0, len(surnames_female) - 1)]
    return ret

def random_phrase():
    n1 = ["Товарищи,", "С другой стороны,", "Равным образом,", "Не следует, однако, забывать, что", "Таким образом,", "Повседневная практика показывает, что"]
    n2 = ["реализация намеченных плановых заданий", "рамки и место обучения кадров", "постоянный количественный рост и сфера нашей активности", "сложившаяся структура организации", "новая модель организационной деятельности", "дальнейшее развитие различных форм деятельности"]
    n3 = ["играет важную роль в формировании", "требует от нас анализа", "требуют определения и уточнения", "способствует подготовке и реализации", "обеспечивает широкому кругу участие в формировании", "позволяет выполнить важные задания по разработке"]
    n4 = ["существенных финансовых и административных условий", "дальнейщих направлений развития", "системы массового участия", "позиций, занимаемых участниками в отношении поставленных задач", "новых предложений", "направлений прогрессивного развития"]
    ret = n1[random.randint(0, len(n1) - 1)] + ' ' + n2[random.randint(0, len(n2) - 1)] + ' ' + n3[random.randint(0, len(n3) - 1)] + ' ' + n4[random.randint(0, len(n4) - 1)]
    return ret
