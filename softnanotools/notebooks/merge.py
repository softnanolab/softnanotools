#!/usr/bin/env python
"""
Merge a list of IPython Notebooks
"""
from _core import IPythonCell, IPythonNotebook
from _utils import IPythonTools

_description = """
Merges a list of IPython Notebooks
"""

def main(files, **kwargs):
    IPythonTools.merge(files, **kwargs)
    return

def _parser():
    import argparse
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('files', nargs='+', help='List of .ipynb files')
    parser.add_argument('-o', '--out')
    return parser

if __name__ == '__main__':
    parser = _parser()
    args = parser.parse_args()
    main(args.files, **args)
