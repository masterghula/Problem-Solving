class BankAccount:
    def __init__(self, customer_name, account_number, opening_balance, overdraft_limit):
        self.customer_name=customer_name
        self.account_number=account_number
        self.opening_balance=opening_balance
        self.overdraft_limit=overdraft_limit
        self.current_balance=opening_balance

    def printdetails(self):
        print("Customer name is ", self.customer_name)
        print("Accound number is ", self.account_number)
        print("Opening balance is ", self.opening_balance)
        print("Overdraft limit is", self.overdraft_limit)

    def checklimit(self,amount):
        if (self.current_balance-amount)>self.overdraft_limit:
            return True
        else:
            return False

    def deposit(self, amount):
        self.current_balance+=amount
        print("Current balance is now: ", self.current_balance)

    def withdraw(self, amount):
        if self.checklimit(amount):
            self.current_balance-=amount
            print("Current balance now is: ", self.current_balance)
        else:
            print("Insufficient funds")


