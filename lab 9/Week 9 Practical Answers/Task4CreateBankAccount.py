from Task4 import *


def main():
    name = input("Enter customer Name: ")
    accNo = input("Enter Account Number: ")
    openBal = int(input("Enter Opening Balance: "))
    overLimit = -(int(input("Enter Overdraft Limit: ")))

    bankAccount1 = BankAccount(name, accNo, openBal, overLimit)

    bankAccount1.printOpenAccount()

    userChoice = 'y'

    while userChoice == 'y':
        print("")
        option = int(input("Enter 1 to deposit or 2 to withdraw: "))

        if option == 1:
            amount = input("Enter the amount you want to deposit: ")
            bankAccount1.deposit(amount)
        elif option == 2:
            amount = input("Enter the amount you want to withdraw: ")
            bankAccount1.withdraw(amount)
        else:
            print("Invalid choice")

        userChoice = input("Do you want to do another transaction? ('y' for yes): ")

    print("Your final balance is", bankAccount1.currentBal)


main()
