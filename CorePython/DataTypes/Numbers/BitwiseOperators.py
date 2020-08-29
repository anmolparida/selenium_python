"""
Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
For example, 2 is 10 in binary and 7 is 111.
"""
x = 10 # 0000 1010
y = 4  # 0000 0100

print(x & y)    # 0000 0010 - 0
print(x | y)    # 0000 1010 - 14
print(-x)       # 1111 0101 -
