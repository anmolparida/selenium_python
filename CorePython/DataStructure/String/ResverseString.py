"""
reversed_string = string [::-1]
Slice notation "[a:b:c]" means "count in increments of c starting at a inclusive, up to b exclusive".
If c is negative you count backwards, if omitted it is 1.
If a is omitted then you start as far as possible in the direction you're counting from (so that's the start if c is positive and the end if negative).
If b is omitted then you end as far as possible in the direction you're counting to (so that's the end if c is positive and the start if negative).
If a or b is negative it's an offset from the end (-1 being the last character) instead of the start.

OK, so string[0::-1] is one character, it says "count backwards from index 0 as far as you can". As far as it can is the start of the string.

"""


def ReverseString_method1(string):
    print(string[::-1])


ReverseString_method1("ANMOLPARIDA")


def ReverseString_method2(string):
    rev_string = ""
    for letter in string:
        rev_string = letter + rev_string

    print(rev_string)


ReverseString_method2('ANMOL')
