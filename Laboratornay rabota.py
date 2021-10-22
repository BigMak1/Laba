with open('pokemon_full.json') as file:
    # Task1

    string = file.read()  # Делаем из файла строку
    chars_amount = len(string)
    print(f'1)Общее количество символов: {chars_amount}')

    # Task 2

    chars_amount1 = 0  # Будем записывать количество символов без пробелов и знаков препинания
    for count in string:
        if count.isalnum():  # Находим символы, которые не являются знакоми препинания
            chars_amount1 += 1
    print(f'2)Общее количество символов без знаков препинания: {chars_amount1}')

    # Task 3

    file.seek(0)
    suma = 0  # Будем считать количество символов в строке "description" текущего покемона
    name = ''  # Будем записывать имя текущего покемона
    max_suma = 0  # Будем хранить максимальное кол-во символов
    max_name = ''  # Будем хранить имя покемона с максимальным кол-вом
    while True:
        line = file.readline()  # Читаем файл по строкам
        if not line:
            break
        line = line.strip()  # Убираем пробелы пред строкой
        if 'name' in line:
            name = line
        if 'description' in line:
            suma = len(line)
            if suma > max_suma:
                max_suma = sum
                max_name = name
    max_name = max_name[9:-2:1]  # Убираем лишние символы из строки
    print(f'3)Самое длинное описание у {max_name}')

    # Task 4

    file.seek(0)
    counter = 0  # Заведем индификато(счетчик) того, что у нас перечисляются способности покемона
    space = 0  # Будем записывать количество пробелов в строке со способностью
    max_space = 0  # Будем хранить максимальное количество пробелов в строке, то есть максимальное кол-во слов
    max_ability = ''  # Будем хранить способность с максимальным кол-вом слов
    while True:
        line1 = file.readline()  # Читаем файл по строкам
        if not line1:
            break
        line1 = line1.strip()  # Убираем пробелы пред строкой
        if '],' in line1:
            counter = 0
        if counter == 1:
            space = line1.count(' ') - line1.count(' "')  # Вычитаем пробелы, которые идут перед ковычками
            if space >= max_space:
                max_space = space
                max_ability = line1
        if 'abilities' in line1:
            counter = 1
    max_ability = max_ability[1:-1]  # Убираем кавычки из ответа
    print(f'4)Умение, которое содержит больше всего слов - это {max_ability}')
