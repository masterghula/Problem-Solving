import random
rand=int(input("How many random numbers do you want to generate: "))
limit=int(input("Whats the maximum number you want: "))
cut=int(input("How many numbers do you want to cut off: "))
lst=[]
for i in range(rand):
    n=random.randint(1,limit)
    lst.append(n)
print("Unsorted list\n",lst)
lst.sort()
print("Sorted list\n",lst)
new_list=[]
for done in range(cut,rand-cut+1):
    new_list.append(lst[done])
print("Cutted\n",new_list)