"""
Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""


def pattern_star_right_arrow_method1(n):
    print('pattern_star_right_arrow_method1')
    for i in range(n + 1):
        print("* " * i)

    for j in range(n - 1, 0, -1):
        print("* " * j)


pattern_star_right_arrow_method1(5)


def pattern_star_right_arrow_method2(n):
    print('pattern_star_right_arrow_method2')
    for i in range(n):
        for j in range(i):
            print('* ', end=' ')
        print('')

    for i in range(n, 0, -1):
        for j in range(i):
            print('* ', end=' ')
        print('')


pattern_star_right_arrow_method2(5)
