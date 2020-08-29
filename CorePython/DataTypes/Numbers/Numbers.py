"""
Python supports integers, floating-point numbers and complex numbers.
They are defined as int, float, and complex classes in Python.
"""

a = 5
print(type(a))
print(a + 3)

b = 5.0
print(type(b))
print(b + 3)

c = 5 + 0j
print(type(c))
print(complex(c))
print(c + 3)
print(c + 999j)
print(c + 10 + 14j)

print(isinstance(c, int))

print("\nType Conversion int ")
print(int(a))
print(int(b))
# print(int(c)) -- can't convert complex to int

print("\nType Conversion float ")
print(float(a))
print(float(b))
# print(float(c)) -- can't convert complex to float

print("\nType Conversion complex ")
print(complex(a))
print(complex(b))
print(complex(c))