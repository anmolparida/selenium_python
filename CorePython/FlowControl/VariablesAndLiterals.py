"""
Literals : Literal is a raw data given in a variable or constant. In Python, there are various types of literals they are as follows:

Numeric Literals : Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.

Unicode is a standard encoding system that is used to represent character from almost all languages.
Each character is encoded using a unique integer code point between 0 and 0x10FFFF .
A Unicode string is a sequence of zero or more code points.

"""

#############################

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2

#Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

#############################

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

#############################

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#############################

drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

# print(d.__doc__)

d = {'a':'apple',
     'b':'blade',
     'c': 'cloud'}

print(d)
print(d.keys())
print(d.values())
print(d.get('b'))
print(d['a'])
print(d.items())

# Getting key name from the value
val = 'blade'
for key, value in d.items():
    if val == value:
        print(key)
print('key does not exist')

