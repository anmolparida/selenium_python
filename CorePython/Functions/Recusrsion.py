"""
Recursion is the process of defining something in terms of itself.

A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

By default, the maximum depth of recursion is 1000. If the limit is crossed, it results in RecursionError.
"""

def factorial_recusrsion(num):
    """recursive function to find the factorial of a number"""
    if num == 1:
        return 1
    else:
        return num * factorial_recusrsion(num-1)

print(factorial_recusrsion(5))


def factorial_loop(num):
    if num == 1:
        return 1
    else:
        output = 1
        while num > 0:
            output =  output * num
            num -=1
        return  output

print(factorial_loop(5))
