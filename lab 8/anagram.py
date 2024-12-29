str1="Earth"
str2="Heart"

lst1=[]
lst2=[]

str1=str1.upper()
str2=str2.upper()

for n in str1:
    lst1.append(n)
for n in str2:
    lst2.append(n)

lst1.sort()
lst2.sort()

if lst1==lst2:
    print("They are anagrams")
else:
    print("Not anagrams")