from CorePython.GlobalVariable import config
from CorePython.GlobalVariable import update
import math
from math import *
# prints the list of methods in module update

print(dir(update))

"""
Python Module Search PATH
PYTHONPATH (an environment variable with a list of directories).
"""
import  sys
for path in sys.path:
    print(path)
