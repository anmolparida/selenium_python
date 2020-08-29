# 25-August-2020 05:30 PM
# Interviewers Pasha Yakub & Priyanka

# Question 1
# [Polymorphism] Same method names with different implementations in different class


class BMW:

    def make(self):
        print("This is a BMW")

    def fuel(self):
        print('Runs on Petrol')


class Tesla:

    def make(self):
        print("This is a Tesla")

    def fuel(self):
        print('Runs on Electricity')


# Common Interface
def autoTest(car):
    car.make()
    car.fuel()


# instantiate object
b = BMW()
t = Tesla()

# Passing the Object
autoTest(b)
autoTest(t)

# Question 2
# [List Manipulation] - Reverse sentence without reversing letters, words only

inputStr = 'i love python'
outputStr = 'python love i'

newStr = []

for words in inputStr.split():
    newStr.insert(0, words)
print(" ".join(newStr))

# Question 3
# [Operators] Interchange values without a 3rd variable
x, y = 10, 100
print(x, y)

y, x = x, y
print(x, y)

# Question 4
# [Data Structure] Create a Dictionary from 2 lists of same length

l1 = ["A", "B", "C", "D"]
l2 = ["1", "2", "3", "4"]

# Method 1 - Using zip
print(dict(zip(l1, l2)))

# Method 2 - using for loop
d = {}

for key in l1:
    for val in l2:
        d[key] = val
        l2.remove(val)
        break
print(d)
