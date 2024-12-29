from Shapes import *


def main():
    dimension = float(input("Enter dimension: "))
    triangle1 = Triangle()

    print("The area of the square is", triangle1.getArea(dimension))
    print("The boundary of the square is", triangle1.getBoundary(dimension))
    print("The number of shapes created:", Shape.getCount())
    print("The number of triangles created:", Triangle.getCount())


main()
