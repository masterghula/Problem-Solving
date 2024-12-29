from Shapes import *


def main():
    dimension = float(input("Enter dimension: "))
    circle1 = Circle()

    print("The area of the square is", circle1.getArea(dimension))
    print("The boundary of the square is", circle1.getBoundary(dimension))
    print("The number of shapes created:", Shape.getCount())
    print("The number of circles created:", Circle.getCount())


main()
