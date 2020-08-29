"""
Count the number of even and odd numbers from a series of numbers
Input
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
Output
Number of even numbers : 4
Number of odd numbers : 5

"""

def count_even_odd(vInput):

    count_odd = 0
    count_even = 0
    for number in vInput:
        if number % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1

    print('count_even: ', count_even)
    print('count_odd', count_odd)


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Declaring the tuple
count_even_odd(numbers)

