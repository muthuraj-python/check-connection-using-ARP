"""
    Module for Router connectivity using ARP
"""

import sys
import json
import argparse

import logger
from cisco_iosxr import CiscoIOSXR
from device import Device

def is_connected(device_1: Device, device_2: Device) -> bool:
    '''
    Print d1.ip <-> d2.ip if both router's are connected.

            Parameters:
                    d1 (Device): Instance of Device
                    d1 (Device): Instance of Device

            Returns:
                    bool (bool): True if d1 neighbor entry in d2 local_infomation else False
    '''
    for neighbor in device_1.arp.neighbors:
        for local_information in device_2.arp.local_informations:
            if neighbor['ip'] == local_information['ip']:
                logger.debug(f'{device_1.ip} neighbor \
                    {json.dumps(neighbor, indent=4)} available in \n{device_2.ip} \
                        local information {json.dumps(local_information, indent=4)}')
                return True
    return False

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-d1", "--device1", dest="d1",
                  help="Device 1 confiuration file name, format shoud be x.x.x.x_22")
    parser.add_argument("-d2", "--device2", dest="d2",
                      help="Device 2 confiuration file name, format shoud be x.x.x.x_22")
    parser.add_argument("-t1", "--type-1", dest="device_1_type", default="CiscoIOSXR",
                  help="Device 1 Type default is CiscoIOSXR")
    parser.add_argument("-t2", "--type-2", dest="device_2_type", default="CiscoIOSXR",
                  help="Device 2 Type default is CiscoIOSXR")
    args = parser.parse_args()

    if not args.d1:
        logger.error(
            "please pass device 1 configuration file, for more details run\n \
                    'python check_connection.py --help'")
        sys.exit(0)
    if not args.d2:
        logger.error("please pass device 2 configuration file, for more details run\n \
                    'python check_connection.py --help'")
        sys.exit(0)

    if args.device_1_type == 'CiscoIOSXR':
        device_1 = CiscoIOSXR(args.d1)
    if args.device_2_type == 'CiscoIOSXR':
        device_2 = CiscoIOSXR(args.d2)
    else:
        raise NotImplementedError

    if is_connected(device_1, device_2):
        logger.info(device_1.ip + '<->' + device_2.ip)
