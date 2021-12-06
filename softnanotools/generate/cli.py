import argparse

from ..logger import Logger
logger = Logger(__name__)

from . import _script, _module

def run(command: str, kind: str, name: str, **kwargs):
    assert command == 'generate'
    if kind == 'script':
        _script.generate(name)
    elif kind == 'module':
        _module.generate(name)
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('kind')
    parser.add_argument('name')
    args = parser.parse_args()
    run('generate', **vars(args))
    return