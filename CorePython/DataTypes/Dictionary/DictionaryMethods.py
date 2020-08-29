d =  {'A': 1, 'B' : 2}
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d.get('A'))
print(d['A'])

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)

# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print(my_dict)

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)

"""
Removing elements from Dictionary
"""

print('\nRemoving elements from Dictionary')
# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

squares[4] = 16
print(squares)

# removes last item, return (key,value)
# Output: (5, 25)
print(squares.popitem())
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares
# print(squares) # Throws Error


"""
setdefault
"""
person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)