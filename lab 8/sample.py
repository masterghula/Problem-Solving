sample_file=open("sample.txt","r")
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
print("\n", setofwords)

