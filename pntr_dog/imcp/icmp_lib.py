""" ICMP library for Pointer_Dog
to validate the presence of specified IPs
Base on rfc792 http://tools.ietf.org/html/rfc792
and rfc 1071 https://www.ietf.org/rfc/rfc1071.txt
"""

import struct
import os
import socket
import random

from .icmp_exceptions import BadOSUserException

ICMP_ECHO = 8

def get_checksum(packet):

    tmp_sum = 0
    count = len(packet)
    i = 0

    while count > 1:
        tmp_sum += (packet[i] * 256) + packet[i+1]
        i += 2
        count -= 2

    if count > 0:
        tmp_sum += packet[i]
        tmp_sum = tmp_sum & 0xffffffff

    while(tmp_sum>>16):
        tmp_sum = (tmp_sum & 0xffff) + (tmp_sum >> 16)

    #csum = tmp_sum >> 8 | (tmp_sum << 8 & 0xff00)
    return tmp_sum#csum

def get_packet(id):
    print(id)
    #8bit, 8bit, U16bit, U16bit, 16bit
    pack_format = 'bbHHh'

    #get 32bytes of char
    with open("/dev/urandom", 'rb') as f:
        data = f.read(32)

    # data = 32 * 'B'

    seq = 1

    #See RFC792 "Echo or Echo reply message""
    header = struct.pack(pack_format, ICMP_ECHO, 0, 0, id, seq)

    checksum = get_checksum(header + data)

    #redo the header with the checksum
    header = struct.pack(pack_format, ICMP_ECHO, 0, checksum, id, seq)

    return header + data

def icmp_call(ip_addr):
    icmp = socket.getprotobyname("icmp")
    id = os.getpid() & 0xFFFF
    packet = get_packet(id)
    if os.getuid() == 0:
        # if root do the perfect ping
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    else:
        raise BadOSUserException('Root')

    #sock.connect((ip_addr, 7))
    #icmp_response_handler(sock,id)

    return False

def icmp_response_handler(sock,id):
        pass
