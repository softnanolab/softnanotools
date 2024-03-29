"""Container for the Logger class.

Classes:
    Logger: tool for logging
    NewLineFormatter:
        formatter for the logger, ensuring prefixes can be easily
        added on each new line

"""
import logging
import os
from pathlib import Path

from typing import Union


class NewLineFormatter(logging.Formatter):
    """Custom Formatter to allow newlines when printing long log messages"""

    def __init__(self):
        """Initialise with normal logging format string."""
        logging.Formatter.__init__(self, "%(levelname)s: [%(name)s] %(message)s")

    def format(self, record) -> str:
        """Formatter to ensure that new lines include the prefix."""
        msg = logging.Formatter.format(self, record)

        if record.message != "":
            parts = msg.split(record.message)
            msg = msg.replace("\n", "\n" + parts[0])

        return msg


class Logger:
    """Smart logger with formatting.

    The default logging level is INFO, to allow debug
    statements, create the following environment variable
    ```
    export DEBUG_LEVEL=10
    ```

    Parameters:
        name: name of the logger (appears in every message)
        logfile: optional path to logfile where data will be written

    >>> import softnanotools.logger
    >>> logger = softnanotools.logger.Logger(__name__)
    >>> logger.debug('Debug Message')
    >>> logger.info('Info Message')
    >>> logger.warning('Warning Message')
    >>> logger.error('Error Message')
    >>> logger.kill('Error Message')
    """

    def __init__(self, name: str, logfile: Union[str, Path] = None):
        """Initialise using filename or custom name."""
        if name == "__main__":
            name = "root"
        self.logger = logging.getLogger(name)
        self.logger.propagate = False
        self.logger.setLevel(int(os.environ.get("DEBUG_LEVEL", logging.INFO)))

        # manage default logging to stdout
        ch = logging.StreamHandler()
        ch.setFormatter(NewLineFormatter())
        self.logger.addHandler(ch)

        # >>> add option for file logging

        # if not given try and get from environment variable
        if not logfile:
            logfile = os.environ.get("LOGFILE", False)

        # create file handler (fh) and add to logger
        if logfile:
            fh = logging.FileHandler(logfile)
            fh.setFormatter(NewLineFormatter())
            self.logger.addHandler(fh)

    @property
    def level(self):
        return self.logger.level

    @level.setter
    def level(self, value):
        self.logger.setLevel(value)

    def debug(self, message):
        """Print a debug message for DEBUG_LEVEL<=10."""
        self.logger.debug(message)

    def info(self, message):
        """Print an info message for DEBUG_LEVEL<=20."""
        self.logger.info(message)

    def warning(self, message: str):
        """Print a warning message for DEBUG_LEVEL<=30."""
        self.logger.warning(message)

    def error(
        self,
        message: str,
        error: Exception = SystemError,
        exception: Exception = None
    ):
        """Print an error message for DEBUG_LEVEL<=40.

        Args:
            message: message for logger to print
            error: the error that should be raised
            exception: any previous exceptions that caused the error

        Raises:
            Exception: (default SystemError)
        """
        self.logger.error(message)
        if exception is None:
            raise error(message)
        else:
            raise error(message) from exception

    def kill(
        self,
        message: str,
        exception: Exception = None
    ):
        """Kill program and print message for DEBUG_LEVEL<=50.

        Args:
            message: message for logger to print
            error: the error that should be raised
            exception: any previous exceptions that caused the error

        Raises:
            Exception: (default SystemExit)
        """
        self.logger.critical(message)
        if exception is None:
            raise SystemExit(message)
        else:
            raise SystemExit(message) from exception
