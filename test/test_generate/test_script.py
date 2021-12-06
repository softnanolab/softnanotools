#!/usr/bin/env python
"""Tests softnanotools.generate._script
"""
from pathlib import Path
import softnanotools.generate._script as script

TARGET = Path(__file__).parent / 'example.py'

def test_script():
    container = script.Script('example.py')
    container.string
    return

def test_generate():
    script.generate(TARGET)
    TARGET.unlink()
    return

if __name__ == '__main__':
    test_script()
    test_generate()