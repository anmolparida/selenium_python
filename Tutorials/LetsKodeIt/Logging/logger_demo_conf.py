import logging
import logging.config

class LoggerDemoConf():

    def testLog(self):

        # create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        self.logging.debug('debug')
        self.logging.warning('warning')

demo = LoggerDemoConf
demo.testLog()