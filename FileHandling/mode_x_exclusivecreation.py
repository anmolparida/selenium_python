try:
    with open("test2.txt", mode = 'x', encoding='utf-8') as f:
        print('File Created')
except FileExistsError:
        print('File already exists')


