"""
We need to be careful with the w mode, as it will overwrite into the file if it already exists.
Due to this, all the previous data are erased.
"""

with open("test.txt", mode= 'w', encoding='utf-8') as f:
    # prints everything in the same line if \n is not mentioned
    print('name:', f.name)
    print('fileno:', f.fileno())
    print('is atty - interactive: ', f.isatty())
    f.write('Line 0 ')
    f.write('continued ')
    f.write('Header Line')

    for i in range(1, 6):
        line = 'Line ' + str(i)
        f.write('\n'+line)

    print('lines written into file')

    f.flush()