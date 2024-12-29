class house:
    def __init__ (self, address, floors, doors, heating):
        self.address = address
        self.floors = floors
        self.doors = doors
        self.heating = heating

    def printdetails(self):
        print("House details: ")
        print("Address is ", self.address)
        print("There are ", self.floors, " floors")
        print("There are ", self.doors, " doors")
        print("The heating is ", self.heating)