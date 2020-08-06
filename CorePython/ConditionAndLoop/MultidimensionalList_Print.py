# Printing a mutidimensional Array

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]

print('*#*#*# Method 1 *#*#*#')
for record in a:
    for value in record:
        print(value, end=' ')
    print()

print('*#*#*# Method 2 *#*#*#')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

