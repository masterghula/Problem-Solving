from task4 import *
customer_name=input("Customer name: ")
account_number=input("Account number: ")
opening_balance=int(input("Opening balance: "))
overdraft_limit=int(input("Overdraft limit: "))

account1=BankAccount(customer_name, account_number, opening_balance, overdraft_limit)
account1.printdetails()

account1.deposit(500)
account1.withdraw(1000)