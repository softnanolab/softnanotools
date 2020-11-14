"""
The `logger` module contains a logger class that
allows users to simply track their code by including
statements that are printed to the terminal.

Logging is important for tracking the progress of code.
However, building loggers to use within packages is
not trivial. To manage this, we have a simple logger
which is initialised at the start of a file.

classes:
    Logger - A logger for printing to the terminal

"""

from ._logger import Logger