import math
class shapes:
    __count=0
    def __init__(self, area, boundary):
        self.area=area
        self.boundary=boundary
        shapes.__count+=1

    def get_area(self,dimension):
        return 0
    def get_boundary(self):
        return 0

class squares(shapes):
    __count_square=0
    def __init__(self):
        super().__init__()
        squares.__count_square+=1

    def get_area(self, length):
        self.area=length * length
        return self.area

    def get_boundary(self, length):
        self.boundary=4 * length
        return self.boundary