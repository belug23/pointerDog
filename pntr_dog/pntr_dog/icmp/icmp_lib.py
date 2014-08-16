""" ICMP library for Pointer_Dog
to validate the presence of specified IPs
Base on rfc792 http://tools.ietf.org/html/rfc792
and rfc 1071 https://www.ietf.org/rfc/rfc1071.txt
"""

import struct
import os
import socket
import random

ICMP_ECHO = 8

def get_cheksum(packet):
    return 0

def get_packet(id):

    #8bit, 8bit, U16bit, U16bit, 16bit
    pack_format = 'bbHHh'

    #get 32bytes of random char
    with open("/dev/random", 'rb') as f:
        data = f.read(32)

    seq = 1

    #See RFC792 "Echo or Echo reply message""
    header = struct.pack(pack_format, ICMP_ECHO, 0, 0, id, seq)

    checksum = get_checksum(header + data)

    #redo the header with the checksum
    header = struct.pack(pack_format, ICMP_ECHO, 0, checksum, id, seq)

    return header + data

def icmp_call(ip_addr):
    id = random.random() % 65535
    send_icmp_request(id)
    get_icmp_response(id)

    return False

def send_icmp_request(id):
    packet = get_packet(id)
    pass

def recive_icmp_response():
    pass
