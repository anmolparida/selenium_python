import subprocess

winFilePath = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium_Python\\FileFolderTerminals\\"

# Specific to Mac

# for i in range(0,5):
#     subprocess.check_call(['python3','Example.py'])
#     # subprocess.check_call(['python3', winFilePath + 'Example.py'])

# Specific to Windows

import sys
import subprocess

theproc = subprocess.Popen([sys.executable, 'Example.py'])
theproc.communicate()