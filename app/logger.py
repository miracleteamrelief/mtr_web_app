import logging

formatter = logging.Formatter('%(levelname)-8s %(filename)s:%(lineno)d:%(funcName)s %(message)s  %(asctime)s')
logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

fh = logging.FileHandler('app.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

if __name__ == '__main__':	
	logger.debug('debug msg')
	logger.info('info msg')
	logger.warning('warning msg')
