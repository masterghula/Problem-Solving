from Shapes import *


def main():
    choice = 'y'

    while choice == 'y':

        print("Enter 1 for Square, 2 for Triangle, 3 for Circle:")
        userChoice = int(input("Enter choice: "))
        dimension = float(input("Enter dimension: "))

        if userChoice == 1:
            s1 = Square()
            print("You choose Square")
            print("The area of the square is", s1.getArea(dimension))
            print("The boundary of the square is", s1.getBoundary(dimension))

        elif userChoice == 2:
            s1 = Triangle()
            print("You choose Triangle")
            print("The area of the triangle is", s1.getArea(dimension))
            print("The boundary of the triangle is", s1.getBoundary(dimension))

        else:
            s1 = Circle()
            print("You choose Circle")
            print("The area of the circle is", s1.getArea(dimension))
            print("The boundary of the circle is", s1.getBoundary(dimension))

        choice = input("Do you want to go again? ('y' for yes): ")

    print("The number of shapes created:", Shape.getCount())
    print("The number of squares created:", Square.getCount())
    print("The number of triangles created:", Triangle.getCount())
    print("The number of circles created:", Circle.getCount())

main()
