import argparse

from ..logger import Logger
logger = Logger(__name__)

def run(command: str, **kwargs):
    assert command == 'generate'
    logger.info(kwargs)
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='test')
    args = parser.parse_args()
    run(**vars(args))
    return