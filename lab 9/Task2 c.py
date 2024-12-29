from Task2 import *
count = int(input("How many house details do you want to enter: "))
house_list=[]
for n in range (1, count+1):
    address=input("Enter the address: ")
    floors=int(input("Enter the floors: "))
    doors=int(input("Enter the doors: "))
    heating=input("Enter the type of heating: ")
    house_list.append(house(address, floors, doors, heating))
for n in house_list:
    n.printdetails()
required_address=input("Enter the address you want details for: ")
found="False"
for each in house_list:
    if required_address==each.address:
        print("It is found!")
        each.printdetails()
        found="True"
        break
if found=="False":
    print(":(")