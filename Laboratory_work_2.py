import csv
import requests

asking_words = ['Rating Score', 'Number Votes', 'Tags', 'Type', 'Studios']


def posters(top_names, r_file, file_reader):
    list_ID = []
    if len(top_names) > 5:
        top_names = [top_names[0], top_names[1], top_names[2], top_names[3], top_names[4]]
    for name in top_names:
        r_file.seek(0)
        for line in file_reader:
            if line['Name'] == name:
                list_ID.append(line['Anime-PlanetID'])

    for point in range(len(top_names)):
        ID = list_ID[point]
        url = 'https://www.anime-planet.com/images/anime/covers/thumbs/' + ID + '.jpg'
        img_code = requests.get(url).content
        poster = open(str(point) + '.jpg', 'wb')
        poster.write(img_code)
        poster.close()


def making_poster_top(answer, asking_word, r_file, file_reader, poster_top):
    r_file.seek(0)
    for row in file_reader:
        if answer not in row[asking_word]:
            poster_top.append(row['Name'])
            poster_top.remove(row['Name'])


def run_dialog():
    questions = ['What is your maximum rating score?', 'What is your maximum number votes?',
                 'What genre are you interested in?', 'How do you like to watch anime',
                 'What studios do you like?']
    answer_list = []
    print('Начиная с 3-го вопроса ответы вводить с большой буквы, через запятую,'
          'без разделителей и пробелов')
    for question in questions:
        print(question)
        response = input()
        answer_list.append(response)
    return answer_list


def writing_top(all_names):
    with open('top.txt', 'w', encoding='utf-8') as file:
        for name in all_names:
            file.write(name + '\n')


def making_top(answer_list, r_file, file_reader, all_names):
    top_names = all_names
    if answer_list[0].isdigit():
        r_file.seek(0)
        for row in file_reader:
            if row['Rating Score'] != 'Rating Score' and row['Rating Score'] != 'Unknown':
                if float(answer_list[0]) < float(row['Rating Score']):
                    if row['Name'] in top_names:
                        top_names.remove(row['Name'])

                if answer_list[1].isdigit():
                    if float(answer_list[1]) < float(row['Number Votes']):
                        if row['Name'] in top_names:
                            top_names.remove(row['Name'])
    r_file.seek(0)
    for row in file_reader:
        if row['Rating Score'] != 'Rating Score':
            for genre in answer_list[2].split(','):
                if genre not in row['Tags']:
                    if row['Name'] in top_names:
                        top_names.remove(row['Name'])

            for sort in answer_list[3].split(','):
                if sort not in row['Type']:
                    if row['Name'] in top_names:
                        top_names.remove(row['Name'])

            for stu in answer_list[4].split(','):
                if stu not in row['Studios']:
                    if row['Name'] in top_names:
                        top_names.remove(row['Name'])
    return top_names


def main():
    with open('anime.csv', encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        all_names = []
        for name in file_reader:
            all_names.append(name['Name'])
        answer_list = run_dialog()
        top_names = making_top(answer_list, r_file, file_reader, all_names)
        writing_top(top_names)
        posters(top_names, r_file, file_reader)


if __name__ == '__main__':
    main()
