
with open("test.txt", mode='r', encoding='utf-8') as f:
    # reads the first 5 chars of Second Line
    print(f.read(5))
    # reads the next 5 chars of First Line
    print(f.read(5))
    # read the rest of first line till end
    print(f.read())
    # f.read() returns a newline when end of the line is reached

    # To get the current File Cursor Position
    print(f.tell())

    # Bring file cursor to initial position
    print(f.seek(0))

    # After f.seek(0), f.read() will print everything again
    print(f.read())



"""
Reading a file line by line

1. Using For Loop
2. Using readline() - reads the individual lines of a file
3. Using readlines() - reads the whole content of the file line by line

"""

print('\nReading line Using For Loop\n')

with open("test.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

print('\nReading  line Using readline()\n')
with open("test.txt", mode='r', encoding='utf-8') as f:
    print(f.readline())


print('\nReading Using readlines()\n')
with open("test.txt", mode='r', encoding='utf-8') as f:
    print(f.readlines())
