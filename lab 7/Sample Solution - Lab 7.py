#Practical Lab 7 (2023) - Lists and Tuples

import random

# Task 1
# Design a program that lets a user enter rainfall for 12 months which is then entered into a list.
# The program should process the list to calculate and display the total rainfall for the year, the
# average monthly rainfall, and print out the month number with the highest and lowest amounts of rainfall.

def task1():

    # Local variables
    total = 0.0
    average = 0.0
    highest = 0.0
    lowest = 0.0
    month_lowest = ''
    month_highest = ''

    # List to receive rainfall amounts
    month_rain = [0.0] * 12

    # Initalize a list with names of the months.
    month_list = ['January', 'February', 'March','April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

    length = len(month_list)
    # Get the amount of rainfall for each month.
    tally = 0
    high = month_rain[0] #0.0
    for each_month in range(length): #each_month 0, 1, 2, 3
        month_rain[each_month] = float(input('Enter the rainfall for ' + month_list[each_month] + ": "))
        tally += month_rain[each_month]

        if month_rain[each_month] > high:
            high = month_rain[each_month]

    total = sum(month_rain)

    print("total =", total, "and tally =", tally)

    # Calculate the average.
    average = total / length

    # Calculate the maximum.
    highest = max(month_rain)

    # Get the index of the month with the highest rainfall.
    month_highest = month_rain.index(highest)

    # Calculate the minimum.
    lowest = min(month_rain)

    # Get the index of the month with the lowest rainfall.
    month_lowest = month_rain.index(lowest)

    # Display results
    print('Total rainfall:', format(total, '.2f'))
    print('Average rainfall:', format(average, '.2f'))
    print('Highest rainfall:', month_list[month_highest])
    print('Lowest rainfall:', month_list[month_lowest])

#Task 2
# You will find a file named charge_accounts.txt within the Practical Lab 8 folder on BBL.
# This file contains a list of a company’s valid bank account numbers. Each account number is a seven-digit number,
# e.g. 5658845. Write a program that reads the contents of the file into a list. The program should then ask the
# user to enter a charge account number and determine whether the number is valid by searching for it in the list.
# If the number is in the list, the program should display a message indicating the number is valid. If the number
# is not in the list, the program should display a message indicating the number is invalid.

def task2():
    # Local variables
    search = ''

    try:
        # Open the file for reading
        input_file = open('charge_accounts.txt', 'r')

        accounts = []

        # Strip trailing '\n' from all elements of the list
        for each_record in input_file:
            accounts.append(each_record.rstrip('\n'))

        print("Accounts:", accounts)

        # Get user input
        search = input('Enter the account number to be validated: ')

        # Use in operator to search for the account specified by user
        if search in accounts:
            print('Account number', search, 'is valid.')
        else:
            print('Account number', search, 'is not valid.')

    except IOError:
        print('The file could not be found')
    except:
        print('An error occurred')


#Task 3
#When analysing data it may be desirable to remove the most extreme values before performing other calculations.
# Write a function that takes a list of values and a non-negative integer, n, as its parameters. The function should
# create a new copy of the list with the n largest elements and n smallest elements removed. Then it should return the
# new copy of the list as the function result. Test your program by declaring a list and a value for n, which you
# pass to the function. NOTE: The order of the elements in the returned list does not need to match the order of the
# original list.

def task3():

    num = int(input('How many random numbers do you want to generate? '))

    list = []
    for i in range(num):
        n = random.randint(1,10)
        list.append(n)

    print("Generated list:", list)

    list.sort()
    print("Sorted list:", list)
    new_list = []

    n=3 #number to 'cut off' each end.

    for each_item in range(3,len(list)-2):
        new_list.append(list[each_item])

    print("New list:", new_list)

#Task 4
# When writing out a list of items in English, one normally separates the items with commas. In addition,
# the word ‘and’ is normally included before the last item, unless the list only contains one item.
# Consider the following examples: Car / Car and boat / Car, boat and bikes / Car, boat, bike and plane
# Write a function that takes a list of strings as its only parameter. Your function should return a string that
# contains all of the items in the list formatted in the manner described previously as its only result. Include
# a main program that reads several items from the user, formats them by calling your function, and then displays
# the result returned by the function.

def task4(string_list):

    # format the list
    list_len = len(string_list)
    string_builder = ''
    if list_len <=1:
        string_builder = string_list[0]
    else:
        for i in range(list_len):
            if i == list_len-1:
                string_builder = string_builder + str(string_list[i])
            elif i == list_len - 2:
                string_builder = string_builder + string_list[i] + ' and '
            else:
                string_builder = string_builder + string_list[i] + ', '

    print(string_builder)


# MAIN PROGRAM

selection = ''

while(selection != '0'):
    selection = input('\nWhich task do you want to execute? ')
    if(selection == '1'):
        task1()
    elif(selection == '2'):
        task2()
    elif(selection == '3'):
        task3()
    elif(selection == '4'):
        string_list = []
        words = ''
        while words != 'end':
            words = input('Add a word to the list: ')
            if words != 'end':
                string_list.append(words)
        task4(string_list)
