rain_file = open("rain.txt","w")
months=[]
total=0
for i in range (1,13):
    rain=float(input("Enter the rainfall for month "+str(i)+": "))
    total+=rain
    months.append(rain)
max_value=max(months)
min_value=min(months)
print("max is",max_value)
print("min is", min_value)
print("Total rain is", total)
print(months)