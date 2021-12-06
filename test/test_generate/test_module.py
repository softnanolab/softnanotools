#!/usr/bin/env python
"""Tests softnanotools.generate._module
"""
from pathlib import Path
import softnanotools.generate._module as module

TARGET = Path(__file__).parent / 'example.py'

def test_Module():
    container = module.Module('example.py')
    container.string
    return

def test_generate():
    module.generate(TARGET)
    TARGET.unlink()
    return

if __name__ == '__main__':
    test_Module()
    test_generate()