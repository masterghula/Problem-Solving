# This program uses the for loop to read
# all of the values in the sales.txt file
# and returns their sum as the total sales

def main():
    # Open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')

    # initialise total sales to zero
    total = 0.0
    
    # Read all the lines from the file.
    for line in sales_file:
        # Convert line to a float and add to total
        total = total + float(line)
        
    # Format and display the amount.
    print('Total sales: £',format(total, '.2f'),sep='')
        
    # Close the file.
    sales_file.close()

# Call the main function.
main()



