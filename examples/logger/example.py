from softnanotools.logger import Logger

logger = Logger(__name__)
logger.level = 10

def task():
    logger.warning('Random Warning')
    return

def integer_division(x, y):
    logger.debug('Running Integer Division')
    logger.info(f'Dividing {x} by {y}')
    if x % y != 0:
        logger.error(
            f'{x} divided {y} does '
            'not return an integer'
        )
    if y == 0:
        logger.kill('Trying to divide by 0')
    return x / y

def main():
    task()
    try:
        integer_division(1, 2)
    except SystemError:
        logger.warning('Caught System Error')
        
    integer_division(4, 2)
    return
    
if __name__ == "__main__":
    main()