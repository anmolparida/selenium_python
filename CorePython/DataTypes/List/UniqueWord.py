"""

Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red

"""

def UniqueWords_method1(csv):
    csv_list = list((map(str, csv.split(","))))
    for i in range(0, len(csv_list)):
        csv_list.insert(i, csv_list[i].strip())
        csv_list.remove(csv_list[i+1])

    print(sorted(list(set(csv_list))))


UniqueWords_method1("red, white, black, red, green, black")

def UniqueWords_method2(csv):
    csv_list = list((map(str, csv.split(","))))
    d = {}

    for word in csv_list:
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] = d[word] + 1

    for key, value in d.items():
        print(key, value)

    print(sorted(d.keys()))
    print(sorted(d.keys()))
    # print(','.join(d.keys()))


# UniqueWords_method2("red, white, black, red, green, black")