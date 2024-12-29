from Task2 import *


def main():
    houseList = []  # creating an empty list

    userChoice = 'y'

    while userChoice == 'y':
        address = input("Enter the address: ")
        floors = input("Enter the number of floors: ")
        doors = input("Enter the number of doors: ")
        heating = input("Enter the heating type: ")

        houseList.append(House(address, floors, doors, heating))

        userChoice = input("Do you want to add another house? ('y' for yes): ")

    print("No of houses created: ", len(houseList))

    addressValue = input("Enter the address of the house you want to search for: ")
    found = False
    indexValue = 0

    for index in range(len(houseList)):

        if addressValue == houseList[index].address:
            found = True
            indexValue = index

    if found:
        print("House found!")
        houseList[indexValue].printHouse()
    else:
        print("House not found!")


main()
