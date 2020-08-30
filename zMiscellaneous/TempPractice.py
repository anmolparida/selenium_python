
def factorial(n):

    output = 1
    if n >= 1:
        for i in range(1,n+1):
            output = output * i
    print(output)

factorial(5)


