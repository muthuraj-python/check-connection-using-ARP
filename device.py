"""
Module for Device
"""

from arp import Arp
from file_handler import FileHandler

class Device:
    """
    Device class.

    ...

    Attributes
    ----------
    file_name : str
        file name format shuod be <ip>_22; example: 172.29.11.20_22

    """

    def __init__(self, file_name: str):

        self.file_name = file_name
        self.ip, _ = self.file_name.split('_')
        self.file_handler = FileHandler(self.file_name)

    def setup_arp(self, file_handler: FileHandler) -> Arp:
        """ Setup ARP """
        raise NotImplementedError
