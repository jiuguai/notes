import logging

logger = logging.getLogger('zero')

fh = logging.FileHandler('t1.log', encoding='utf-8')
ch = logging.StreamHandler()
ch1 = logging.StreamHandler()
ch.setLevel(logging.ERROR)
logger.addHandler(fh)
logger.addHandler(ch)
logger.addHandler(ch1)
logger.info('zero')