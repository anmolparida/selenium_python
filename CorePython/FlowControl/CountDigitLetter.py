"""

Write a Python program that accepts a string and calculate the number of digits and letters
Sample Data : "Python 3.2"
Expected Output :
Letters 6
Digits 2


"""
def CountDigitLetter(vInput):

    count_alphabet = 0
    count_digits = 0


    for char in vInput:
        if char.isalpha():
            count_alphabet = count_alphabet + 1
        elif char.isdigit():
            count_digits = count_digits + 1

    print('count_alphabet:  ', count_alphabet)
    print('count_digits:    ', count_digits)


CountDigitLetter('ABCD EFGH 9.2.3')