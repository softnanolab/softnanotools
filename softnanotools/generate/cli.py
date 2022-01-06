import argparse
from typing import List

from ..logger import Logger
logger = Logger(__name__)

from . import _script, _module, _package, _project

def run(
    command: str,
    kind: str,
    name: str,
    modules: List[str] = None,
    packages: List[str] = None,
    **kwargs
):
    if modules == None:
        modules = []
    if packages == None:
        packages = []

    assert command == 'generate'
    if kind == 'script':
        _script.generate(name)
    elif kind == 'module':
        _module.generate(name)
    elif kind == 'package':
        _package.generate(name, modules=modules)
    elif kind == 'project':
        _project.generate(name)
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('kind')
    parser.add_argument('name')
    parser.add_argument('-m', '--modules', nargs='+')
    args = parser.parse_args()
    run('generate', **vars(args))
    return