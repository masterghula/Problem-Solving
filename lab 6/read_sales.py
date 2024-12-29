def main():
    #Open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')

    #Read all the lines from the file.
    for line in sales_file:
        #Convert line to a float.
        amount = float(line)
        #Format and display the amount.
        print(format(amount, '.2f'))

    sales_file.close()

main()