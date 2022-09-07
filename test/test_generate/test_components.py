#!/usr/bin/env python
"""Tests softnanotools.generate._components
"""

import softnanotools.generate._components as components

def test_ComponentContainer():
    container = components.ComponentContainer('example.py')
    assert container.name == 'example'
    container.description
    container.logger
    container.docstring
    container.parser
    container.main_function
    container.shebang
    container.doctest_string
    return

def test_FileContainer():
    container = components.FileContainer('example')
    return

if __name__ == '__main__':
    test_ComponentContainer()
    test_FileContainer()