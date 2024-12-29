#Practical Lab 9 (2023) Dictionaries and Sets


# Task1
#Two words are anagrams if they contain all of the same letters, but in a different order.
# For example, ‘Python and ‘Typhon, and ‘Study’ and ‘Dusty’ are anagrams. One way to determine if
# something is an anagram is to tally the individual letters that make up each word, and then to
# compare those tallies. Write and program that reads two words in from the keyboard, determines
# whether or not these are anagrams and produces a report detailing the character make-up of each word.


#APPROACH 1 - just use a list to order two strings and then compare them
def task1a():
    str = 'Earth'
    str2 = 'HEART'

    print(ord('E'), 'vs', ord('e'))

    str = str.upper()
    str2 = str2.upper()

    ls1 = []
    ls2 = []

    for ch in str:
        ls1.append(ch)

    for ch in str2:
        ls2.append(ch)

    ls1.sort()
    ls2.sort()

    print(ls1)
    print(ls2)

    if ls1 == ls2:
        print("True, these strings are anagrams")
    else:
        print('False, these strings are NOT anagrams"')

# APPROACH 2 - use a dictionary to keep tabs on the keys (letters of each word) and the values will be the tally of
# each letter
def task1b():

    dict1 = dict_tally(input('Enter the first word: ').lower())
    dict2 = dict_tally(input('Enter the word that you would like to compare: ').lower())

    print(dict1 == dict2)

def dict_tally(str):
    dict = {}
    for each_ch in str:
        if each_ch in dict:
            dict[each_ch] =  int(dict[each_ch]) + 1
        else:
            dict[each_ch] = 1
    return dict

# Task2
# Morse Code is an encoding scheme that uses dashes and dots to represent numbers and letters.
# In this exercise, you will write a program that uses a dictionary to store the mapping from
# letters and numbers to Morse code. Use a full stop to represent a dot, and a hyphen to represent a dash.
# You will find a copy of the international Morse code on Wikipedia.
#
# Your program should read and message from the user. Then it should translate each letter and number
# in the message to Morse code, leaving a space between each sequence of dashes and dots. Your program
# should ignore any characters that are not letters or numbers. The Morse code for ‘Hello World’ Is shown
# here, as an example: …. . .-.. .-.. --- .-- --- .-. .-. .-..

def task2():
    codes = {'A': '.-',     'B': '-...',   'C': '-.-.',
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',

            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.', ' ': 'SPACE'
            }

    msg = input('MESSAGE: ')
    encrypt(msg, codes)
    msg = input('\nCODE: ')
    decrypt(msg,codes)
    print()


def encrypt(msg, codes):
    for char in msg:
        if char.isspace():
            print('SPACE/',end='')
        elif char.isalpha() or char.isnumeric():
            # code['E']
            print(codes[char.upper()], end='/')

def decrypt(msg, codes):
    tempLetter =''
    word_builder = ''
    for eachMorse in msg:
        if eachMorse !='/':
            tempLetter += eachMorse
        else:
            for each_code in codes:
                # if codes[.] == '.'
                if codes[each_code] == tempLetter:
                    word_builder+=each_code
                    tempLetter =''
    print(word_builder,end='')


# Task 3
# In the game of Scrabble, each letter has points associated with it. The total score of a word is
# the sum of the score of its letters. More common letters are worth fewer points while less common letter
# are worth more points.
# Write a program that computes and displays the score for any word entered. Note: in order to simplify the logic,
# you should use the UPPER() function to convert all words entered into uppercase.

def task3():
    scrabble= {1:['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
              2: ['D', 'G'],
              3: ['B', 'C', 'M', 'P'],
              4: ['F', 'H', 'V', 'W', 'Y'],
              5: ['K'],
              8: ['J','X'],
              10:['Q','Z']
              }

    #students could choose not to use a list though and provide a score per character instead:
    #SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             # "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             # "x": 8, "z": 10} # Capitalized (constant)

    word = input('Enter a word: ').upper()
    word_score = 0

    for ch in word:
        for score, letters in scrabble.items():
            for item in letters:
                if ch == item:
                    word_score += int(score)

    print()
    print(word, 'scores', word_score, 'points')


# Task 4
# Write a program that opens a specified text file and then displays a list of all the unique words
# found in the file. Hint: store each word as an element of a set.

def task4():
    dup_words = open('sample.txt','r')
    set_List = set()
    for each_word in dup_words:
        set_List.add(each_word.rstrip('\n'))
    print(set_List)

def task4b():
    dup_words = open('sample.txt','r')
    set_List = set()

    #split out the words from each line
    temp_line_list = []
    for each_line in dup_words:
        temp_line_list = each_line.split()
        for each_word in temp_line_list:
            set_List.add(each_word.rstrip('\n'))

    print(set_List)

    outfile = open('new_file.txt','w')
    while len(set_List) > 0:
        outfile.writelines(set_List.pop())

# MAIN PROGRAM
selection = ''

while(selection != '0'):
    print()
    print('task 1 - approach1 (1a)')
    print('task 1 - approach2 (1b)')
    print('task 2 - (2)')
    print('task 3 - (3)')
    print('task 4 - (4)')
    print('task 4b - (4b - processing paragraphs)')

    selection = input('\nWhich task do you want to execute? ')
    if(selection == '1a'):
        task1a()
    elif(selection == '1b'):
        task1b()
    elif(selection == '2'):
        task2()
    elif(selection == '3'):
        task3()
    elif(selection == '4'):
        task4()
    elif(selection == '4b'):
        task4b()
    else:
        print('error - retry')







