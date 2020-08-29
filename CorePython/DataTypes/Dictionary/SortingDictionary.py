# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

"""
Solution 1. Creating 3 different methods for 3 different keys
"""
# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print("sort by name (Ascending order)",employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print("sort by Age (Ascending order)",employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print("sort by salary (Descending order)",employees, end='\n\n')


"""
Solution 2. Using Lambda Function instead of keys
"""

print('name ASC', sorted(employees, key= lambda  x : x.get('Name')))
print('age ASC', sorted(employees, key= lambda x : x['age']))
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print('salary DESC',employees)