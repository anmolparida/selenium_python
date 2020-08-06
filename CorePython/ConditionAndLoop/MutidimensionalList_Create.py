# 2 Dimesional List with all Zeros
rows = int(input('number of rows: '))
cols = int(input('number of cols: '))

row_list = []
for i in range(1, rows+1):
    col_list = []
    for j in range(1, cols+1):
        col_list.append(0)
    row_list.append(col_list)
print(row_list)

for val in row_list:
    print(val)

'''

Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.
Input
Input number of rows: 3
Input number of columns: 4
Output [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

'''

rows = int(input('number of rows: '))
cols = int(input('number of cols: '))

row_list = []
for i in range(1, rows+1):
    col_list = []
    for j in range(1, cols+1):
        col_list.append(i*j)
    row_list.append(col_list)

print(row_list)


for val in row_list:
    print(val)








