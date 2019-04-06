import logging

logging.basicConfig(format = '%(asctime)s %(levelname)s: %(message)s',
					level = logging.DEBUG)
logging.debug('This is when it happend')
logging.info('Another time it happend')
logging.warning('And 123 the event occured')