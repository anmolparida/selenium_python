"""
A list can be copied using the = operator. For example,
The problem with copying lists in this way is that if you modify new_list, old_list is also modified.

Shallow Copy - A shallow copy creates a new object which stores the reference of the original elements.
             - Appending changes the New list but extending does not

Deep Copy - A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
            - Appending or extending does not change the list

"""

old_list = [1, 2, 3]
new_list = old_list

# add an element to list
new_list.append(4)

print('New List:', new_list)
print('Old List:', old_list)


# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
new_list = my_list.copy()

print('my_list', my_list)
print('Copied List:', new_list)

"""
shallow copy using the slicing syntax
"""

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)