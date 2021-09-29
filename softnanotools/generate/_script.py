#!/usr/bin/env python
from pathlib import Path
from typing import Union

from ..logger import Logger
logger = Logger(__name__)

def generate(name: str, **kwargs):
    if name.split('.')[-1] != 'py':
        fname = Path(f'{name}.py')
    else:
        fname = Path(name)

    _docstring = f"{name}.py - insert docstring here"

    with open(fname, 'w') as f:
        f.write('#!/usr/bin/env python\n')
        f.write(f'"""{_docstring}"""\n')
        f.write('from softnanotools.logger import Logger\n')
        f.write('logger = Logger(__name__)\n\n')
        f.write('def main(**kwargs):\n')
        f.write(f'    logger.info("Running {name}...")\n')
        f.write('    return\n\n')
        f.write("if __name__ == '__main__':\n")
        f.write('    import argparse\n')
        f.write(
            '    parser = argparse.ArgumentParser('
            f'description="{name}.py")\n'
        )
        f.write('    main(**vars(parser.parse_args()))\n')
    return