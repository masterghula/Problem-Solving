@classmethod
def discount_books_by_author(cls, books, author, discout_percentage):
    total_discount=0 # Blank 1
    for book in books:
        if book.author == author # Blank 2 is author
            original_price=book.price
            discount_amount=book.price*(discount_percentage/100)
            book.price-=discount_amount # Blank 3 is discount_amount
            total_discount+=discount_amount # Blank 4 is total_discount
            print(f"Discounted{book.title} by {author}: ${original_price:.2f} --> ${book.price:.2f}")

