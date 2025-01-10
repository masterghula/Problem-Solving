def tricky(a, b=[]):
    b.append(a)

    return b


print(tricky(1))  # Line 1

print(tricky(2))  # Line 2

print(tricky(3, []))  # Line 3

print(tricky(4))  # Line 4