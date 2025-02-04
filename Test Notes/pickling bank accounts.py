import pickle
details={}
def retrieving():
    required=input("Enter the account number: ")
    if required in details:
        balance=details[required]
        print("That account does exist and its balance is", balance)
    else:
        print("It does not exist")

def pickling():
    file=open("bank.dat", "wb")
    pickle.dump(details, file)
    file.close()

def unpickling():
    file=open("bank.dat","rb")
    loaded_dic=pickle.load(file)
    file.close()
    total=0
    for each in loaded_dic:
        if each[1]>=60000:
            total+=int(each[1])
    print(total)

def main():
    # file=open("bank_accounts.txt","")
    # bank_account=""
    # balance=0
    # for line in file:
    #     parts=line.strip().split(", ")
    #     bank_account, balance = parts[0], parts[1]
    #     details[bank_account]=balance
    # file.close()
    unpickling()
main()