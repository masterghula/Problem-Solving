sample_file=open("sample_words_f (1).txt","r")
word_builder=""
setofwords=set()
for line in sample_file:
    for char in line:
        if char!=" " and char!="\n":
            word_builder+=char
        else:
            print(word_builder, end=" ")
            setofwords.add(word_builder)
            word_builder=""

def letter_tally():
    tally = 0
    for each in setofwords:
        for char in each:
            if char=="t" or char=="T":
                tally+=1
    print("\n", tally)
# letter_tally()

total=len(setofwords)
print("\n", total)
print("\n", setofwords)


