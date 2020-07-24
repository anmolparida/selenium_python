'''

Logging Format

https://docs.python.org/3/library/logging.html
https://docs.python.org/3/library/time.html


'''

import logging

# Logging the messages to a .log file
# logging.basicConfig(filename='test.log', level=logging.DEBUG)

# Formatting the Warnings
# logging.basicConfig(filename="test.log", format='%(levelname)s : %(message)s', level=logging.DEBUG )

# Logging TimeStamp directly to Console
logging.basicConfig(filename="test.log",
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%m-%d-%y %I:%M:%S %p',
                    level=logging.DEBUG)


# Logging Messages
logging.info('info')
logging.warning('warning')
logging.error('error')
