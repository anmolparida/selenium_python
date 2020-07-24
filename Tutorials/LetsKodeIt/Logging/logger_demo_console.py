'''

Logger Demo

'''

import  logging

class LoggerDemoConsole():

    def testLog(self):

        # create logger
        # logger = logging.getLogger('sample_log') # HardCoded
        logger = logging.getLogger(LoggerDemoConsole.__name__) # Generic
        logger.setLevel(logging.INFO)

        # create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s : %(levelname)s : %(message)s',datefmt='%m-%d-%y %I:%M:%S %p')

        # add format to console handler - chandler
        chandler.setFormatter(formatter)

        # add handle to logger
        logger.addHandler(chandler)

        # Logging Messages
        logger.debug('debug message')
        logger.info('warning')
        logger.warning('warning')
        logger.error('error')
        logger.critical('critical')


demo = LoggerDemoConsole()
demo.testLog()