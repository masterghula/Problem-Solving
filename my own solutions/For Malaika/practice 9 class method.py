# Write a function in your Book class that will calculate the average price of the books.
# Once you have done that, fill in the blanks. Please use the following text file, books1.txt,
# for the purposes of testing your code.

@classmethod
def average_price(cls, books):  # Blank 1
    total_price = sum(book.price for book in books)  # Blank 2
    average_price = total_price / len(books)  # Blank 3
    return average_price  # Blank 4
