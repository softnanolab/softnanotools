import logging
import sys
import os

class NewLineFormatter(logging.Formatter):
    """Custom Formatter to allow newlines"""
    def __init__(self):
        """Initialise with normal logging format string"""
        logging.Formatter.__init__(self, '%(levelname)s: [%(name)s] %(message)s')


    def format(self, record) -> str:
        """Formatter to ensure that new lines include the prefix"""
        msg = logging.Formatter.format(self, record)

        if record.message != "":
            parts = msg.split(record.message)
            msg = msg.replace('\n', '\n' + parts[0])

        return msg

class Logger:
    """Smart logger with formatting

    The default logging level is INFO, to allow debug
    statements, create the following environment variable
    ```
    export DEBUG_LEVEL=10
    ```
    
    Usage:
        import softnanotools.logger
        logger = softnanotools.logger.Logger(__name__)
        logger.debug('Debug Message')
        logger.info('Info Message')
        logger.warning('Warning Message')
        logger.error('Error Message')
        logger.kill('Error Message')
    """
    def __init__(self, name: str):
        """Initialise using filename or custom name"""
        if name == '__main__':
            name = 'root'
        self.logger = logging.getLogger(name)
        self.logger.setLevel(
            int(os.environ.get('DEBUG_LEVEL', logging.INFO))
        )
        ch = logging.StreamHandler()
        ch.setFormatter(NewLineFormatter())
        self.logger.addHandler(ch)

    @property
    def level(self):
        return self.logger.level

    @level.setter
    def level(self, value):
        self.logger.setLevel(value)

    def debug(self, message):
        """Print a debug message for DEBUG_LEVEL<=10"""
        self.logger.debug(message)

    def info(self, message):
        """Print an info message for DEBUG_LEVEL<=20"""
        self.logger.info(message)

    def warning(self, message):
        """Print a warning message for DEBUG_LEVEL<=30"""
        self.logger.warning(message)

    def error(self, message):
        """Print an error message for DEBUG_LEVEL<=40"""
        self.logger.error(message)
        raise SystemError(message)

    def kill(self, message=''):
        """Kill program and print message for DEBUG_LEVEL<=50"""
        self.logger.critical(message)
        raise SystemExit(message)

    
