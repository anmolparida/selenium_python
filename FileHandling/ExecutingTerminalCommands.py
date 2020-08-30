import subprocess

winFilePath = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium\\FileHandling\\"

# Specific to Mac

# for i in range(0,5):
#     subprocess.check_call(['python3','FileOperations.py'])
#     # subprocess.check_call(['python3', winFilePath + 'FileOperations.py'])

# Specific to Windows

import sys
import subprocess

theproc = subprocess.Popen([sys.executable, 'FileOperations.py'])
theproc.communicate()