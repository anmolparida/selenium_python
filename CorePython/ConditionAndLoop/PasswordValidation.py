"""
Write a Python program to check the validity of a password (input from users).
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
Input
W3r@100a
Output
Valid password
"""
import re
def validate_passwrod(password):
    if len(password) < 6 or len(password) > 16:
        print("len(password) < 6 or len(password) > 16")
    elif not re.search("[a-z]", password):
        print("[a-z] missing")
    elif not re.search("[A-Z]", password):
        print("[A-Z] missing")
    elif not re.search("[0-9]]", password):
        print("[0-9] missing")
    elif not re.search("[$#@]", password):
        print("[$#@] missing")
    elif not re.search("\s", password):
        print('contains spaces')
    else:
        print('Valid Password: ', password)


validate_passwrod("W3r@100a")