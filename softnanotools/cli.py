from .logger import Logger
logger = Logger(__name__)

def main():
    logger.info("Hello World!")
    return