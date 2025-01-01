from Shapes import *


def main():
    dimension = float(input("Enter dimension: "))
    square1 = Square()

    print("The area of the square is", square1.getArea(dimension))
   # print("The boundary of the square is", square1.getBoundary(dimension))
    print("The number of shapes created:", Shape.getCount())
    print("The number of squares created:", Square.getCount())
    square1.printDetails()


main()
