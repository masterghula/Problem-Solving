def find_max(lst):
    max_value = lst[0] # Initialize max_value with the first list element
    for n in lst: # Iterate through the list
        if n>max_value: # Check if the current number is greater than max_value
            max_value=n# Update max_value to the current number
    return max_value # Return the maximum value
result = find_max([7, 2, 9, 4, 5]) # This is an example list
print(result)
