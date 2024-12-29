class BankAccount:

    def __init__(self, name, accNo, openBal, overLimit):
        self.name = name
        self.accNo = accNo
        self.openBal = openBal
        self.overLimit = overLimit
        self.currentBal = openBal

    def printOpenAccount(self):
        print("")
        print("Account Created!")
        print("Customer Name:", self.name)
        print("Account Name:", self.accNo)
        print("Opening Balance:", self.openBal)
        print("Overdraft Limit:", self.overLimit)

    def deposit(self, amount):

        self.currentBal += int(amount)
        print("The current balance is", self.currentBal)

    def withdraw(self, amount):

        check = self.checkLimit(amount)

        if check:
            print("Overdraft Exceeded!")
            print("This transaction has not gone through")
            print("The current balance is", self.currentBal)
        else:
            self.currentBal -= int(amount)
            print("The current balance is", self.currentBal)

    def checkLimit(self, amount):
        amountCheck = self.currentBal
        amountCheck -= int(amount)
       
        if amountCheck < self.overLimit:
            return True
        else:
            return False
