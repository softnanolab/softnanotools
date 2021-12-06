#!/usr/bin/env python
from pathlib import Path
from typing import Union

from ..logger import Logger
logger = Logger(__name__)

from ._components import ComponentContainer

class Script(ComponentContainer):
    def __init__(self, name):
        super().__init__(name)

    @property
    def logger(self) -> str:
        _logger_name = self.name.upper().replace('_', ' ').replace('-', ' ')
        return super().logger.replace('__name__', f"'{_logger_name}'")

    @property
    def string(self) -> str:
        result = (
            f"{self.shebang}\n"
            f"{self.docstring}\n"
            f"{self.logger}\n"
            f"{self.main_function}\n"
            f"{self.if_name_statement}\n"
            f"{self.parser}\n"
        )
        return result

def generate(name: str, **kwargs):

    script = Script(name)
    with open(script.path, 'w') as f:
        f.write(script.string)

    return