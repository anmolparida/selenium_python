"""
In some situations, you might want to run a certain block of code if the code block inside try ran without any errors.
For these cases, you can use the optional else keyword with the try statement.
"""

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print('reciprocal',reciprocal)