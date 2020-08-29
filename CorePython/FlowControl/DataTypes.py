singleLine = "Single line string"
multiLine = """ Multi line
            string"""

print(singleLine)
print(multiLine)

print(float(5))
print(int(5.0))
print(float(0))
print(int(0.0))
print(float(-5))
print(int(-5.0))

print("#"*50)
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='\n')

# print(input('Enter Name: '))
# evaluates the string inside eval()
print(int(eval('111*11')))

import math
print(math.pi)


print('*#' * 10)
x = True
y = False

print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)