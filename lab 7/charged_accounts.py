accounts_file=open("charge_accounts.txt","r")
accounts_list=[]
for i in accounts_file:
    accounts_list.append(i.rstrip("\n"))
loop="true"
while loop=="true":
    desire = input("What are you looking for: ")
    if desire in accounts_list:
        print("HEHE WE HAVE")
        loop="false"
    else:
        print("HEHE WE DONT HAVE")

accounts_file.close()