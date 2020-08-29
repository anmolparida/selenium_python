"""
A directory must contain a file named __init__.py in order for Python to consider it as a package.
"""

# accessing a method inside a different module in the same or other package

import CorePython
CorePython.Functions.Recusrsion.factorial_loop(5)
# OR #
from CorePython.Functions.Recusrsion import factorial_loop
factorial_loop(5)