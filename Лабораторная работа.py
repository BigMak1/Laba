file1 = open('pokemon_full.json')

# Task1

s = file1.read()  # делаем из файла строку
print('№1')
print(len(s))

# Task 2

kol1 = 0        # количество символов без пробелов и знаков препинания
for i in s:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:    # сравниваем по Юникоду
        kol1 += 1
print('№2')
print(kol1)

# Task 3

file2 = open('pokemon_full.json')
kol2 = 0          # количество символов в строке "description" текущего покемона
name = ''         # имя текущего покемона
maxkol2 = 0       # максимальное кол-во символов
maxname = ''      # имя покемона с максимальным кол-вом
while True:
    line = file2.readline()  # читаем файл по строкам
    if not line:
        break
    line = line.strip()      # убираем пробелы пред строкой
    if "name" in line:
        name = line
    if "description" in line:
        kol2 = len(line)
        if kol2 > maxkol2:
            maxkol2 = kol2
            maxname = name
maxname = maxname[9:-2:1]   # убираем лишние символы из строки
print('№3')
print(maxname)

# Task 4

file3 = open('pokemon_full.json')
ind = 0            # индификатор того, что у нас перечисляются способности покемона
prob = 0           # количество пробелов в строке со способностью
maxprob = 0        # максимальное количество пробелов в строке, то есть максимальное кол-во слов
maxabil = ''       # способность с максимальным кол-вом слов
while True:
    line1 = file3.readline()  # читаем файл по строкам
    if not line1:
        break
    line1 = line1.strip()      # убираем пробелы пред строкой
    if '],' in line1:
        ind = 0
    if ind == 1:
        prob = line1.count(' ') - line1.count(' "')  # вычитаем пробелы, которые идут перед ковычками
        if prob >= maxprob:
            maxprob = prob
            maxabil = line1
    if 'abilities' in line1:
        ind = 1
print('№4')
print(maxabil[1:-1])  # убираем кавычки из ответа
