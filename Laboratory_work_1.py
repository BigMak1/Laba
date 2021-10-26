with open('pokemon_full.json') as file:
    # Task1

    string = file.read()
    chars_amount = len(string)
    print(f'1)Общее количество символов: {chars_amount}')

    # Task 2

    no_punctuation = 0  # Amount of symbol without punctuation
    for char in string:
        if char.isalnum():
            no_punctuation += 1
    print(f'2)Общее количество символов без знаков препинания: {no_punctuation}')

    # Task 3

    file.seek(0)
    dsc_chars = 0  # Contains number of characters in "description" section.
    max_dsc_chars = 0
    current_name = ''
    max_dsc_name = ''
    for line in file:
        line = line.strip()  # Remove whitespase before string
        if 'name' in line:
            current_name = line
        if 'description' in line:
            dsc_chars = len(line)
            if dsc_chars > max_dsc_chars:
                max_dsc_chars = dsc_chars
                max_dsc_name = current_name
    max_dsc_name = max_dsc_name[9:-2]  # Remove needless symbol
    print(f'3)Самое длинное описание у {max_dsc_name}')

    # Task 4

    file.seek(0)
    in_abilities = False
    space_chars = 0  # Contains number of whitespase in string
    max_space_chars = 0
    max_abil_name = ''  # It's an ability with max words
    for line in file:
        line = line.strip()  # Remove whitespase before string
        if '],' in line:
            in_abilities = False
        if in_abilities:
            space_chars = line.count(' ') - line.count(' "')  # Subtract whitespace before current string
            if space_chars >= max_space_chars:
                max_space_chars = space_chars
                max_abil_name = line
        if 'abilities' in line:
            in_abilities = True
    max_abil_name = max_abil_name[1:-1]  # Remove quotation marks in final string
    print(f'4)Умение, которое содержит больше всего слов - это {max_abil_name}')
