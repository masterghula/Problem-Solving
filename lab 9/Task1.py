import math

class circle:
    def __init__ (self, radius):
        self.radius=radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * self.radius * math.pi

circle1=circle(4)
print("The area is", circle1.area())
print("Circumference is", circle1.circumference())