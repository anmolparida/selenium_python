# Write a Python program to get the Fibonacci series between 0 to 50

def fibonaci_first_n_occurence(n):
    fibo_list = [0, 1]
    for i in range(2, n):
        fibo_list.append(int(fibo_list[i - 1]) + int(fibo_list[i - 2]))
    print('Fibonaccci series ' + str(n) + ' ocuurences ', fibo_list)


fibonaci_first_n_occurence(10)


def fibonaci_between_start_end(start, end):
    fibo_list = [0, 1]

    for i in range(2, end + 1):
        fibo_list.append(int(fibo_list[i - 1]) + int(fibo_list[i - 2]))
        if fibo_list[-1] > end:
            print('Fibonaccci series till ' + str(end), fibo_list[:-1])
            break

    fibo_list_range = []
    for val in fibo_list:
        if val in range(start, end+1):
            fibo_list_range.append(val)
    print('Fibonaccci series between  ' + str(start) + ' and ' + str(end), fibo_list_range)


fibonaci_between_start_end(9, 34)


def fibonaci_between_start_end_method_2(end):
    x, y = 0, 1
    fibo_list = [x, y]
    while y <= end:
        fibo_list.append(x + y)
        x, y = y, x + y
    print(fibo_list[:-1])


fibonaci_between_start_end_method_2(34)

