#!/usr/bin/env python
"""Tests softnanotools.generate._project
"""
from pathlib import Path
import softnanotools.generate._project as project

TARGET = Path(__file__).parent / "example"


def clean(folder: Path):
    for f in folder.glob("*"):
        try:
            f.unlink()
        except IsADirectoryError:
            try:
                f.rmdir()
            except OSError:
                clean(f)
                f.rmdir()


def test_generate():
    project.generate("example", root=TARGET)
    clean(TARGET)
    TARGET.rmdir()
    return


if __name__ == "__main__":
    pass
