string_list=[]
words=""
while words!="end":
    words=input("Enter something to the list: ")
    if words!="end":
        string_list.append(words)
new_string=""
list_length=len(string_list)
for i in range (list_length):
    if i==list_length-1:
        new_string = new_string + string_list[i]
    elif i==list_length-2:
        new_string = new_string + string_list[i] + 'and '
    else:
        new_string = new_string + string_list[i] + ', '
print(new_string)