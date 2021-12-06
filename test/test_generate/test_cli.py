#!/usr/bin/env python
"""Tests softnanotools.generate._module
"""
from pathlib import Path
import subprocess

TARGET = Path(__file__).parent / 'example.py'

def test_cli():
    subprocess.check_output(
        ['softnanotools.generate', 'script', TARGET.absolute()]
    )
    subprocess.check_output(
        ['softnanotools.generate', 'module', TARGET.absolute()]
    )
    subprocess.check_output(
        ['softnanotools', 'generate', 'script', TARGET.absolute()]
    )
    subprocess.check_output(
        ['softnanotools', 'generate', 'module', TARGET.absolute()]
    )

    TARGET.unlink()
    return

if __name__ == '__main__':
    test_cli()