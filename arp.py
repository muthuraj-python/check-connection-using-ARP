"""
Module for ARP
"""

class Arp:
    """
    Arp class.

    ...

    Attributes
    ----------
    neighbors : list
        neighbors extracted from arp show command
    local_informations : list
        local_informations extracted from arp show command

    """

    def __init__(self, neighbors: list, local_informations: list):
        self.neighbors = neighbors
        self.local_informations = local_informations

    def get_entries(self) -> list:
        '''
        Get list of ARP entries
        '''
        return self.neighbors + self.local_informations

    def get_entries_count(self) -> int:
        '''
        Get total entries count in ARP
        '''
        return len(self.neighbors + self.local_informations)
