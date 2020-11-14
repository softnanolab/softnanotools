from softnanotools.logger import Logger

def test_Logger():
    logger = Logger(__name__))
    logger.debug('DEBUG')
    logger.info('INFO')
    logger.warning('WARNING')
    logger.error('ERROR')
    try:
        logger.kill('KILL')
    except SystemExit:
        continue
    return