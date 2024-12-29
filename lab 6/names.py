name_file = open("names.txt","r")
count = len(name_file.readlines())
print("There are ",count,"names")
search=input("Enter the name you want to search: ")
name_file.seek(0)
tally=0
for line in range(count):
    current=name_file.readline().rstrip()
    if current.upper() == search.upper():
        tally +=1
print("The name occurs",tally,"times")