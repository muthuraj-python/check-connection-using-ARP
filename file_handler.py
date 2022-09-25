"""
Module for read file
"""

import sys

import logger


class FileHandler:
    """
    FileHandler class, to read device confuguration file

    ...

    Attributes
    ----------
    file_name : str
        Name of the configuration file

    """

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.list_of_lines_from_file = self._read_file()
        logger.debug(f"Successfully read a {self.file_name}")

    def _read_file(self) -> list:
        '''
        Return readlines from file
        '''

        try:
            with open(self.file_name, 'r') as file:
                return file.readlines()
        except FileNotFoundError as err:
            logger.error(f"File {self.file_name} not in current dir..!")
            sys.exit(0)
