"""
Strings are immutable.
Forzensets are immutable version of the set

This means that elements of a string cannot be changed once they have been assigned.
We can simply reassign different strings to the same name.

"""
my_string = 'programiz'
# my_string[5] = 'a'    # TypeError: 'str' object does not support item assignment - not mutable
# del my_string[1]      # TypeError: 'str' object doesn't support item deletion

"""
enumerate 
 
The enumerate() function returns an enumerate object. 
It contains the index and value of all the items in the string as pairs. This can be useful for iteration.
"""

s = 'PYTHON'

list_enumerate = list(enumerate(s))
print('list_enumerate', list_enumerate)
print(list_enumerate[0][1])

# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.

# my_set = {1, 2, [3, 4]}
"""
Set can have any number of items and they may be of different types (integer, float, tuple, string etc.). 
But a set cannot have mutable elements like lists, sets or dictionaries as its elements.
"""

# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))

# initialize a with set()
a = set()

# check data type of a
print(type(a))

# initialize my_set
my_set = {1, 3}
print(my_set)

# my_set[0] # TypeError: 'set' object does not support indexing

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)

"""
Difference between discard() and remove()
my_set.remove(2)    - remove throws  key error if element is not present in set
my_set.discard(2)   - discard does not throw error if element is not present in th set

"""
print('\n Difference between discard() and remove()')
# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

# my_set.remove(2)

# initialize my_set - Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element - Output: random element unlike last element in list
print(my_set.pop())

# pop another element
print(my_set.pop())

# clear my_set - Output: set()
my_set.clear()
print(my_set)

"""
SET Properties
"""
print('\nSET Properties')
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A.union(B))

print(A.intersection(B))
print(A & B)

# Values only present in A
print(A.difference(B))
print(A-B)

# Values only present in B
print(B.difference(A))
print(B-A)

# All elements in A.union(B) excluding A.intersection(B)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

# symmetric_difference simplified
print(A.union(B) - A.intersection(B))
