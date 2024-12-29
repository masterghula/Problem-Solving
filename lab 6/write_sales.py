def main():
    num_days = int(input('How many days do you have sales: '))
    sales_file = open('sales.txt', 'w')
    for count in range(1,num_days+1):
        print('Enter the sales for day#'+str(count)+':')
        men_sales = float(input('Enter men sales: '))
        women_sales = float(input('Enter women sales: '))
        children_sales = float(input('Enter children sales: '))
        total = men_sales + women_sales + children_sales
        print('Total for today is', total)
        sales_file.write(str(men_sales)+'\n'+str(women_sales)+'\n'+str(children_sales)+'\n'+str(total)+'\n')
    sales_file.close()
    print("Data written to sales.txt: ")
main()