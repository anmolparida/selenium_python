

winFilepath = "C:\\Users\\aparida\\OneDrive\\Code\\Coding\\Pyhton\\Course Files\\Python_Automation_Files\\Exercise Files\\"
# macFilepath

f = open(winFilepath + "inputFile.txt", 'r')

passFile = open(winFilepath + 'PassFile.txt', 'w')
failFile = open(winFilepath + 'FailFile.txt', 'w')

# print(f.read())

count = 0

for line in f:
    line_split = line.split()

    if line_split[-1] == 'P': # we need to find the names of the people who have passed the test
        count = count + 1
        print(str(count), line)
        passFile.write(line)

    elif line_split[-1] == 'F':  # we need to find the names of the people who have passed the test
        count = count + 1
        print(str(count), line)
        failFile.write(line)

f.close() # always close the file