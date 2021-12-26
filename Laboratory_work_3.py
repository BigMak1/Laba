from bdfparser import Font

data_file = Font('light_pixel-7.bdf')


def print_chr(list):

    for string in list:
        bin_string = bin(int(string, 16))[2:]
        design_string = ''
        for binary in bin_string:
            if binary == '1':
                binary = '$'
            else:
                binary = ' '
            design_string += binary
        print(design_string)


with open('your_word.tiff', 'wb') as image:
    data_sign = data_file.glyphs
    word = input()
    for letter in word:
        chr = data_sign[ord(letter)][-1]
        print_chr(chr)
        print()
