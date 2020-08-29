"""
- Lambda function is a small anonymous function
- Lambda function is used when we need it shorter period of time
- Lambda function can take any number of arguments but only one expression
- Lambda function does not have a return statement, always have a expression which is returned

- Why use Lambda Function ?
    - we can use lambda function as an anonymous function inside a function
    - Ex: We have a function definition that takes one argument, that argument will be multiplied with an unknown number

Syntax : lambda arguments : expression

- The filter() function in Python takes in a function and a list as arguments.  -- returns values which are True
- The map() function in Python takes in a function and a list as arguments.     -- returns all values
- The reduce() function in Python takes in a function and a list as argument.
"""

add = lambda  a : a + 10
print(add(5))

multiply = lambda a, b  : a * b
print(multiply(5,6))

def power(n):
  return lambda a : pow(a, n)

square = power(2)
cube = power(3)

print(square(11))
print(cube(11))

# Create a lambda function that takes one parameter (a) and returns it.
print((lambda a : a)('XYZ'))

output = lambda a : a
print(output("ABC"))


# Python code to illustrate filter() with lambda()
print('\nPython code to illustrate filter() with lambda()\n ')

input_list = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9]

odd_list =  list(filter(lambda x : (x%2 != 0), input_list))
even_list = list(filter(lambda x : (x%2 == 0), input_list))

print(odd_list)
print(even_list)


# Python code to illustrate map() with lambda()
print('\nPython code to illustrate map() with lambda()')

input_list = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]

remainder_list = list(map(lambda x : x%2, input_list))
print(remainder_list)


input_list = [1,2,3,4,5,6,7,8,9,10]
odd_list = list(filter(lambda x : x%2 != 0, input_list))    # only values which are true are returned after evaluation
even_list = list(map(lambda x: x%2 == 0, input_list))       # all values are returned after evaluation

print(odd_list)
print(even_list)


from functools import reduce
# Python code to illustrate reduce() with lambda()
print('\nPython code to illustrate reduce() with lambda()')

print("Sum of numbers in the given range: ", end="")
output = reduce(lambda x, y: x+y, range(1,101))
print(output)

print("Sum of numbers in the given range: ", end="")
output = reduce(lambda x, y: x+y, [1,2,3,4,5,5,20])
print(output)


def sumInRange(start, end):
  total = 0
  for x in range(start,end+1):
    total = total + x
  print("Sum of numbers in the given range {0} and {1} is : {2}".format(start, end,total))

sumInRange(1,100)

# Sum of a Given List
li = [5, 8, 10, 20, 50, 100]
output = reduce(lambda x, y : x + y, li )
print(output)