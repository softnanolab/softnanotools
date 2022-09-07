import argparse

from .logger import Logger
logger = Logger(__name__)

from .generate.cli import run as generate_cli

_DESCRIPTION = "Welcome to softnanotools CLI!"

_CLI_MAP = {
    'generate': generate_cli
}

def main():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    parser.add_argument('command')
    parser.add_argument('args', nargs='+', metavar='args')
    args = parser.parse_args()
    _CLI_MAP[args.command](args.command, *args.args)
    return