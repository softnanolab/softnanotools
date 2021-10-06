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
    try:
        logfile.unlink()
    except FileNotFoundError:
        print(f'Tried to delete {logfile} but it did not exist')
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
    with open(logfile, 'r') as f:
        logger_name = f.readline().split()[1]

    expected_output = [
        f"DEBUG: {logger_name} DEBUG\n",
        f"INFO: {logger_name} INFO\n",
        f"WARNING: {logger_name} WARNING\n",
        f"ERROR: {logger_name} ERROR\n",
        f"DEBUG: {logger_name} Successfully caught error\n",
        f"CRITICAL: {logger_name} KILL\n",
        f"DEBUG: {logger_name} Successfully caught kill\n",
    ]

    with open(logfile, 'r') as f:
        for i, line in enumerate(f.readlines()):
            assert expected_output[i] == line

    logfile.unlink()
    return