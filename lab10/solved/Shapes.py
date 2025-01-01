import math


class Shape:
    __count = 0

    def __init__(self):
        self.area = None
        self.boundary = None
        Shape.__count += 1

    def getArea(self, length):
        return 0

    def getBoundary(self, length):
        return 0

    @classmethod
    def getCount(cls):
        return Shape.__count

    def printDetails(self):
        print("Area:", self.area)
        print("Boundary", self.boundary)


class Square(Shape):
    __countSquare = 0

    def __init__(self):
        super().__init__()
        Square.__countSquare += 1

    def getArea(self, length):
        self.area = length * length
        return self.area

    def getBoundary(self, length):
        self.boundary = 4 * length
        return self.boundary

    @classmethod
    def getCount(cls):
        return Square.__countSquare


class Triangle(Shape):
    __countTriangle = 0

    def __init__(self):
        super()._init__()
        Triangle.__countTriangle += 1

    def getArea(self, length):
        self.area = 0.5 * length * length
        return self.area

    def getBoundary(self, length):
        self.boundary = (2 * length) + math.sqrt(2 * length * length)
        return self.boundary

    @classmethod
    def getCount(cls):
        return Triangle.__countTriangle


class Circle(Shape):
    __countCircle = 0

    def __init__(self):
        super()._init__()
        Circle.__countCircle += 1

    def getArea(self, length):
        self.area = length * length * math.pi
        return self.area

    def getBoundary(self, length):
        self.boundary = 2 * length * math.pi
        return self.boundary

    @classmethod
    def getCount(cls):
        return Circle.__countCircle
