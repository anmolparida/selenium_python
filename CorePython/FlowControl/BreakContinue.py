a = 3
while a < 5:
    print(a)
    a += 1

print("The end")

# Program to show the use of continue statement inside loops
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")


for val in "string":
    if val == "i":
        break
    print(val)

print("The end")