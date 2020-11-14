from softnanotools.logger import Logger

def test_Logger():
    logger = Logger(__name__)
    logger.level
    logger.level = 10
    logger.debug('DEBUG')
    logger.info('INFO')
    logger.warning('WARNING')
    logger.error('ERROR')
    try:
        logger.kill('KILL')
    except SystemExit:
        logger.debug('Successfully caught kill')
    return