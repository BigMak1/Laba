import csv

with open("anime.csv", encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=",")
    all_names = []
    for name in file_reader:
        all_names.append(name['Name'])

    def making_top(answer, asking_word):
        r_file.seek(0)
        for row in file_reader:
            if answer not in row[asking_word]:
                all_names.append(row['Name'])
                all_names.remove(row['Name'])

    questions = ['How many rating score do you have?', 'How many number votes do you have?',
                 'What genre are you interested in?', 'What themes do you want to see?',
                 'How do you like to watch anime', 'What season would you like to watch from?',
                 'What studios do you like?']
    asking_words = ['Rating Score', 'Number Votes', 'Tags', 'Content Warning',
                    'Type', 'Season', 'Studios']
    for index in range(len(questions)):
        print(questions[index])
        response = input()
        if response == ' ' or response == '':
            continue
        else:
            making_top(response, asking_words[index])
    with open('top.txt', 'w', encoding='utf-8') as file:
        for name in all_names:
            file.write(name + '\n')

    # POSTERS

    # Find ID our 5 first names
    list_ID = []
    top5_names = [all_names[0], all_names[1], all_names[2], all_names[3], all_names[4]]
    for name in top5_names:
        r_file.seek(0)
        for line in file_reader:
            if line['Name'] == name:
                list_ID.append(line['Anime-PlanetID'])

    # Download 5 picture
    import requests

    for point in 1, 2, 3, 4, 5:
        ID = list_ID[point-1]
        url = 'https://www.anime-planet.com/images/anime/covers/thumbs/' + ID + '.jpg'
        img_code = requests.get(url).content
        poster = open(str(point) + '.jpg', 'wb')
        poster.write(img_code)
        poster.close()
