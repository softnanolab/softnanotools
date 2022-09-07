#!/usr/bin/env python
"""Tests softnanotools.generate._module
"""
from pathlib import Path
import softnanotools.generate.cli as cli

TARGET = Path(__file__).parent / 'example.py'

def test_run():
    cli.run('generate', 'script', TARGET.absolute())
    cli.run('generate', 'module', TARGET.absolute())
    TARGET.unlink()
    return

if __name__ == '__main__':
    test_run()