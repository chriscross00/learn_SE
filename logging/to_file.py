import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to log file')
logging.info('The log file should be clear')
logging.warning('And should be the only one')

