#!/usr/bin/env python
from pathlib import Path
from typing import Union

from ..logger import Logger
logger = Logger(__name__)

def generate(fname: Union[Path, str], **kwargs):
    with open(fname, 'w') as f:
        f.write('#!/usr/bin/env python\n\n')
        f.write('from softnanotools.logger import Logger\n')
        f.write('logger = Logger(__name__)\n\n')
        f.write('def main(**kwargs):\n')
        f.write('    return\n\n')
        f.write("if __name__ == '__main__':\n")
        f.write('    import argparse\n')
        f.write('    parser = argparse.ArgumentParser()\n')
        f.write('    main(**vars(parser.parse_args()))\n')
    return