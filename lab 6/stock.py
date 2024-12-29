stock_file = open("stock.txt","r")
count=len(stock_file.readlines())
print("The total days are",count)
stock_file.seek(0)
largest = float(stock_file.readline())
total = largest
for num in range(count-1):
    current = float(stock_file.readline())
    total += current
    if current>largest:
        largest=current
print("The largest is",largest)
print("Averge is", total/count)
stock_file.close()
