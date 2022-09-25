"""
Device Module for CISCO-IOSXR

"""
import json

import logger
from device import Device
from arp import Arp
from file_handler import FileHandler

class ArpExtractorHandler:
    """
    ArpExtractorHandler class.

    ...

    Attributes
    ----------
    list_of_lines_from_file : list
        list of lines from configuration line

    """


    def __init__(self, ip: str, list_of_lines_from_file: list):
        self.ip = ip
        self.list_of_lines_from_file = list_of_lines_from_file
        self.neighbors_list = []
        self.local_informations_list = []

    def get_neighbors(self) -> list:

        ''' Filter neighbors from arp a command output'''

        neighbors = [line.strip() for line in self.list_of_lines_from_file \
                                if 'Dynamic' in line and 'ARPA' in line]
        for neighbor in neighbors:
            ip, _, mac, _, _, inf_name = [i for i in neighbor.split(' ') if i.strip()]
            self.neighbors_list.append({
                                'ip':ip,
                                'mac': mac,
                                'inf_name': inf_name})
        logger.debug(f"Successfully extracted {self.ip} neighbors. \n \
                                    {json.dumps(self.neighbors_list, indent=4)}")
        return self.neighbors_list

    def get_local_informations(self) -> list:
        ''' Filter local_informations_from arp a command output'''

        local_informations = [line.strip() for line in self.list_of_lines_from_file \
                            if 'Interface' in line and 'ARPA' in line]
        for local_information in local_informations:
            #import ipdb;ipdb.set_trace()
            ip, _, mac, _, _, inf_name = [i for i in local_information.split(' ') if i.strip()]
            self.local_informations_list.append({
                                'ip':ip,
                                'mac': mac,
                                'inf_name': inf_name})
        logger.debug(f"Successfully extracted {self.ip} local_informations. \
                        {json.dumps(self.local_informations_list, indent=4)}")
        return self.local_informations_list


class CiscoIOSXR(Device):
    '''
    CiscoIOSXR class.
    '''

    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.arp = self._setup_arp(self.file_handler)

    def _setup_arp(self, file_handler: FileHandler) -> Arp:
        ''' Setup ARP details for device '''
        self.arp_extractor_handler = ArpExtractorHandler(self.ip,
                                file_handler.list_of_lines_from_file)
        self.arp = Arp(self.arp_extractor_handler.get_neighbors(),
                                self.arp_extractor_handler.get_local_informations())
        logger.debug(f'{self.ip} ARP Neighbours details \
                                    {json.dumps(self.arp.neighbors, indent=4)}')
        logger.debug(f'{self.ip} ARP Local Information details \
                            {json.dumps(self.arp.local_informations, indent=4)}')
        return self.arp
