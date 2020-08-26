"""
Write a Python program to construct the following pattern, using a nested loop number.
1
22
333
4444
55555
666666
7777777
88888888
999999999

"""
vInput = 9

for i in range(vInput + 1):
    print(str(i) * i)
