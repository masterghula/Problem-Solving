# This program allows the user to modify the quantity
# in a record in the coffee.txt file.

import os  # Needed for the remove and rename functions

def main():
    choice=int(input("Enter 1 for modifying and anything for searching"))
    if choice == 1:
        # Create a bool variable to use as a flag.
        found = False

        # Get the search value and the new quantity.
        search = input('Enter a description to search for: ')
        new_qty = int(input('Enter the new quantity: '))
        new_roast = input('Enter the new roast: ')
        new_type = input('Enter the new type')

        # Open the original coffee.txt file.
        coffee_file = open('coffee.txt', 'r')

        # Open the temporary file.
        temp_file = open('temp.txt', 'w')

        # Read the first record's description field.
        descr = coffee_file.readline()

        # Read the rest of the file.
        while descr != '':
            # Read the quantity field.
            qty = float(coffee_file.readline())
            roast = coffee_file.readline().rstrip()
            coffee_type = coffee_file.readline().rstrip()
            # Strip the \n from the description.
            descr = descr.rstrip('\n')

            # Write either this record to the temporary file,
            # or the new record if this is the one that is
            # to be modified.
            if descr == search:
                # Write the modified record to the temp file.
                temp_file.write(descr + '\n')
                temp_file.write(str(new_qty) + '\n')
                temp_file.write(new_roast + '\n')
                temp_file.write(new_type + '\n')
                # Set the found flag to True.
                found = True
            else:
                # Write the original record to the temp file.
                temp_file.write(descr + '\n')
                temp_file.write(str(qty) + '\n')
                temp_file.write(roast + '\n')
                temp_file.write(coffee_type + '\n')

            # Read the next description.
            descr = coffee_file.readline()

        # Close the coffee file and the temporary file.
        coffee_file.close()
        temp_file.close()

        # Delete the original coffee.txt file.
        os.remove('coffee.txt')

        # Rename the temporary file.
        os.rename('temp.txt', 'coffee.txt')

        # If the search value was not found in the file
        # display a message.
        if found:
            print('The file has been updated.')
        else:
            print('That item was not found in the file.')
    else:
        search = input('Enter the roast to search for: ')
        tally = 0
        having=[]
        coffee_file = open('coffee.txt', 'r')
        descr = coffee_file.readline()
        # Read the rest of the file.
        while descr != '':
            qty = float(coffee_file.readline())
            roast = coffee_file.readline().rstrip()
            coffee_type = coffee_file.readline().rstrip()
            # Strip the \n from the description.
            roast = roast.rstrip('\n')
            if roast == search:
                tally +=1
                having.append(descr)
            descr = coffee_file.readline()
        print ("number of coffees that have that roast is", tally)
        print("They are", having)
# Call the main function.
main()
