"""
Logger module for logging
"""

import logging

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fhandler = logging.FileHandler(filename='debug.log', mode='a')
fhandler.setFormatter(formatter)
fhandler.setLevel(logging.DEBUG)

shandler = logging.StreamHandler()
shandler.setFormatter(formatter)
shandler.setLevel(logging.INFO)

logger.addHandler(fhandler)
logger.addHandler(shandler)

logger.setLevel(logging.DEBUG)


def info(message: str) -> bool:
    ''' To print info messages '''

    logger.info(message)


def warn(message: str) -> bool:
    ''' To print warning messages '''

    logger.warning(message)


def debug(message: str) -> str:
    ''' To print Debug messages '''

    logger.debug(message)


def error(message: str) -> bool:
    ''' To print Error messages '''

    logger.error(message)
