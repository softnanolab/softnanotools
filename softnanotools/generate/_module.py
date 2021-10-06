#!/usr/bin/env python
from pathlib import Path
from typing import Union

from ..logger import Logger
logger = Logger(__name__)

from ._components import ComponentContainer

class Module(ComponentContainer):
    def __init__(self, name):
        super().__init__(name)

    @property
    def string(self) -> str:
        result = (
            f"{self.shebang}\n"
            f"{self.docstring}\n"
            f"{self.logger}\n"
            f"{self.if_name_statement}\n"
            f"{self.doctest_string}\n"
        )
        return result

def generate(name: str, **kwargs):
    if name.split('.')[-1] != 'py':
        fname = Path(f'{name}.py')
    else:
        fname = Path(name)

    module = Module(name)

    with open(fname, 'w') as f:
        f.write(module.string)

    return