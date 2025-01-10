condition="True"
while condition=="True":
    num=int(input("Enter an even number: "))
    if num%2==0:
        total=0
        for n in range(0, num+1, 2):
            total+=n
        condition="False"

print(total)