# driverLocation = "/Users/AnmolParida/OneDrive/Code/Python/Selenium/Drivers/chromedriver"


lst = [[1, 2, 3], [1, 1, 2], [4, 5, 1], 4, 5, 3]


def unique(inputList):
    d = {}
    for x in range(len(inputList)):
        print(inputList[x])
        for y in range(len(inputList[x])):
            print(inputList[x][y])
            # if x[y] in d:
            #     d[x[y]] = d[x[y]] + 1
            # else:
            #     d[x[y]] = 1
    print(d)


unique(lst)




