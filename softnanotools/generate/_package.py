#!/usr/bin/env python
"""_package.py - auto-generated by softnanotools"""
from pathlib import Path
from typing import List
import softnanotools.generate._module as module

from softnanotools.logger import Logger
logger = Logger(__name__)

def generate(
    name: str, modules: List[str] = ["example"], packages: List[str] = None, **kwargs
):
    """"""
    if modules is None:
        modules = []
    if packages is None:
        packages = []

    package = Path(name)
    package.mkdir(exist_ok=True)

    __INIT__ = package / "__init__.py"

    if not __INIT__.exists():
        with open(__INIT__, "w") as f:
            f.write(f'"""Welcome to {name}!\n"""')

    for m in modules:
        components = m.split(".")
        if len(components) > 1:
            logger.debug(f"For module {m}, created components: {components}")
            for p in components[:-2]:
                generate(p)
            generate(package / components[-2], modules=[components[-1]])
        else:
            module.generate(package / components[-1])

    return


if __name__ == "__main__":
    import doctest

    doctest.testmod()
