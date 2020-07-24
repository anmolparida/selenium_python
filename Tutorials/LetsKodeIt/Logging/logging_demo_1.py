"""
--Does not Print--
Logging Demo1 
Logging Levels
DEBUG
INFO

--Prints--
WARNING 
ERROR
CRITICAL

"""

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.info('info message')
logging.warning('warning message')
logging.error('error message')