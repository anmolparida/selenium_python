"""
Python List Methods

append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of the number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list

"""
even = [2, 4, 6, 8, 8 ]
print(even.index(8)) # Returns the index of the first matched item
print(even.count(8)) # Returns the count of the number of items passed as an argument

# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# Change/Replace the 1st item
odd[0] = 1
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]
print(odd)

odd.append(9)
print(odd)

# Extends one or multiple items
odd.extend([11,13,15])
print(odd)

# Extends one or multiple items
odd.extend([[17], [19, 21]])
print(odd)

odd.extend([[23,25], [], 'END'])
print(odd)

odd = odd + [31]
print(odd)

print(['repeat'] * 3)

# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)
print(odd)

# inserting a slice of multiple items
odd[2:2] = [5, 7]
print(odd)


"""
Delete Remove Pop elements from List
"""
print('\nDelete Remove Pop elements from List')
lst = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

del lst[2]  # removes the element at index 2 - o
print(lst)

lst = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
lst.remove('o') # removes the element directly - no index needed - o
print(lst)

lst = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print(lst.pop(2))  # pop takes out the element at the index - o

lst = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print(lst.pop())  # pop without index takes out the last element of the list

lst = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
lst.clear() # removes all elements and gives an empty list
print(lst)


