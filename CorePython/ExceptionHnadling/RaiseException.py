try:
    a = int(input('Enter a positive number: '))
    if a <= 0:
        raise ValueError (a, "is no a positive integer")
except ValueError as ve:
    print(ve)

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError (a ,"is not a positive number!")
except ValueError as ve:
    print(ve)