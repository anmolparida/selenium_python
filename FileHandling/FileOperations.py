"""
Mode	Description
r	    Opens a file for reading. (default)
w	    Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	    Opens a file for exclusive creation. If the file already exists, the operation fails.
a	    Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	    Opens in text mode. (default)
b	    Opens in binary mode.
+	    Opens a file for updating (reading and writing)
"""

# Creating file at current directory
# Opens a file for exclusive creation. If the file already exists, the operation fai

# f = open("test.txt", x)

# Opening file at specific directory
f = open('/Users/AnmolParida/OneDrive/Code/Python/Selenium/FileHandling/test.txt')

# Opening file current directory
f = open("test.txt", 'r')
f = open("test.txt", 'w')


"""
Hence, when working with files in text mode, it is highly recommended to specify the encoding type.
"""
f = open("test.txt", mode='r', encoding='utf-8')


"""
Closing file in Python

f.close()
This method is not entirely safe.
If an exception occurs when we are performing some operation with the file, the code exits with out closing the file.
"""

# Best way to open and close files in Python

try:
    f = open("test.txt", mode='r', encoding='utf-8' )
    # Perform file operations
finally:
    f.close()

"""
The  best way to close a file is by using with statement.
This ensures that the file is closed when the block inside the with statement  is exited.
"""

with open("test.txt", mode= 'r', encoding = 'utf-8') as f:
    # perform file operations
    pass
    # we dont need to explicitly close() the method, it is done internally.

