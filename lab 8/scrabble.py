scrabble= {1:['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
              2: ['D', 'G'],
              3: ['B', 'C', 'M', 'P'],
              4: ['F', 'H', 'V', 'W', 'Y'],
              5: ['K'],
              8: ['J','X'],
              10:['Q','Z']
              }
counter=0
word=input("Enter the word: ").upper()
for eachletter in word:
    for score, list in scrabble.items():
        for eachlistletter in list:
            if eachlistletter==eachletter:
                counter+=score
print(counter)