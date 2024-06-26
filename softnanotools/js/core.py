#!/usr/bin/env python
"""core.py - auto-generated by softnanotools"""
import json
from pathlib import Path
from typing import Any, List
from softnanotools.logger import Logger
logger = Logger(__name__)

def parse_key(key: str, sep: str = '.') -> List[str]:
    keys = key.split(sep)
    return keys

class JSONReader:
    """A JSONReader stores file information about a JSON file"""
    def __init__(self, fname: Path):
        self.fname = fname
        self.data = {}
        self.raw = ""
        self.read()

    def read(self):
        """Sets JSONReader.data and JSONReader.raw by opening and
        reading JSONReader.fname"""
        with open(self.fname, 'r') as f:
            string = f.read()
            self.raw = string
            self.data = json.loads(string)
        return

    def write(self, output: Path):
        """Writes JSONReader.data to file"""
        with open(output, 'w') as f:
            json.dump(self.data, f, indent=2)
        return

    @staticmethod
    def replace(fname: Path, key: str, value: Any, **kwargs):
        """Reads a JSON file and replaces any key with a new value"""
        reader = JSONReader(fname)
        keys = parse_key(key)
        ## THIS IS A HACK - NEEDS TO BE IMPROVED
        if len(keys) == 1:
            reader.data[keys[0]] = value
        elif len(keys) == 2:
            reader.data[keys[0]][keys[1]] = value
        elif len(keys) == 3:
            reader.data[keys[0]][keys[1]][keys[2]] = value
        elif len(keys) == 4:
            reader.data[keys[0]][keys[1]][keys[2]][keys[3]] = value
        else:
            raise NotImplementedError(
                'Automated nesting not implemented '
                '- current nesting limit is 4-levels!'
            )
        reader.write(fname)
        return



if __name__ == '__main__':
    import doctest
    doctest.testmod()
