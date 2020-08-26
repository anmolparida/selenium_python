a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]


a.insert(0, [1, 3, 5, 7])
a.extend([5, 6, [9, 10]])  # extend can add multiple elements to the list
a.append([7, 8])    # append can add one element/list

print(a)

# a[0].append(33)
# a[0].extend([44, 55])
# a[0].insert(0, 1111)

# print(a)

# a[0].clear()

# print(a)
