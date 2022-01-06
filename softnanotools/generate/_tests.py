#!/usr/bin/env python
"""Generate a pytest suite with example test file
"""
from softnanotools.logger import Logger
logger = Logger(__name__)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
