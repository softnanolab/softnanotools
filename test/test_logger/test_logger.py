from softnanotools.logger import Logger
from pathlib import Path

def test_Logger():
    logger = Logger(__name__)
    logger.level
    logger.level = 10
    logger.debug('DEBUG')
    logger.info('INFO')
    logger.warning('WARNING')
    try:
        logger.error('ERROR')
    except SystemError:
        logger.debug('Successfully caught error')
    try:
        logger.kill('KILL')
    except SystemExit:
        logger.debug('Successfully caught kill')
    return

def test_Logger_with_filehandler():
    # initialise logger with file
    logfile = Path(__file__).parent / 'test.log'
    logfile.unlink()
    logger = Logger(__name__, logfile=logfile)

    # do the same as above
    logger.level
    logger.level = 10
    logger.debug('DEBUG')
    logger.info('INFO')
    logger.warning('WARNING')
    try:
        logger.error('ERROR')
    except SystemError:
        logger.debug('Successfully caught error')
    try:
        logger.kill('KILL')
    except SystemExit:
        logger.debug('Successfully caught kill')

    # check expected output with details of file

    expected_output = [
        "DEBUG: [test.test_logger.test_logger] DEBUG\n",
        "INFO: [test.test_logger.test_logger] INFO\n",
        "WARNING: [test.test_logger.test_logger] WARNING\n",
        "ERROR: [test.test_logger.test_logger] ERROR\n",
        "DEBUG: [test.test_logger.test_logger] Successfully caught error\n",
        "CRITICAL: [test.test_logger.test_logger] KILL\n",
        "DEBUG: [test.test_logger.test_logger] Successfully caught kill\n",
    ]
    
    with open(logfile, 'r') as f:
        for i, line in enumerate(f.readlines()):
            assert expected_output[i] == line

    logfile.unlink()
    return