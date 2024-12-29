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

    for index in houseList:
        index.printHouse()


main()
