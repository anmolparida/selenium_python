import os

# get current working directory
print(os.getcwd())
print(os.getcwdb())

# change directory
os.chdir("/Users/AnmolParida/OneDrive/Code/Python/Selenium/")
print(os.getcwd())
os.chdir("/Users/AnmolParida/OneDrive/Code/Python/Selenium/FileHandling")
print(os.getcwd())

# list all files and folders in the directory
print(os.listdir())
print(list(enumerate(os.listdir())))

for files in sorted(list(enumerate(os.listdir()))):
    print(files)

# list all files and folders in the specified directory
print(os.listdir("/Users/AnmolParida/OneDrive/Code/Python/Selenium/"))

# Creating a new directory/folder
try:
    os.mkdir('FolderName')
    print(os.listdir())
except FileExistsError:
    print('Directory already exists')

# renaming the directory
os.chdir("/Users/AnmolParida/OneDrive/Code/Python/Selenium//FileHandling/DirOuter")
print(os.getcwd())
print(os.listdir())
os.rename('DirInner', 'InnerDirectory')
print(os.listdir())
os.rename('InnerDirectory', 'DirInner')

