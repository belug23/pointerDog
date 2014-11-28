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
#8bit, 8bit, U16bit, U16bit, 16bit
pack_format = 'bbHHh'

def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)

def get_checksum(packet):
   s = 0
   for i in range(0, len(packet), 2):
       w = packet[i] + (packet[i+1] << 8)
       s = carry_around_add(s, w)
   return ~s & 0xffff

def get_packet(id):

    #get 32bytes of char
    with open("/dev/urandom", 'rb') as f:
        data = f.read(32)

    # data = 32 * 'B'
    # data = data.encode('utf-8')
    # print(data)

    seq = 1

    #See RFC792 "Echo or Echo reply message""
    header = struct.pack(pack_format, ICMP_ECHO, 0, 0, id, seq)

    checksum = get_checksum(header + data)

    #redo the header with the checksum
    header = struct.pack(pack_format, ICMP_ECHO, 0, checksum, id, seq)

    return header + data

def icmp_call(ip_addr):
    # print(ip_addr)
    ip_addr = socket.gethostbyname(ip_addr)
    # print(ip_addr)
    icmp = socket.getprotobyname("icmp")
    id = os.getpid() & 0xFFFF
    packet = get_packet(id)
    if os.getuid() == 0:
        # if root do the perfect ping
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    else:
        raise BadOSUserException('Root')
    sock.settimeout(9)
    while packet:
        chunk_size = sock.sendto(packet,(ip_addr, 0))
        packet = packet[chunk_size:]
    return icmp_response_handler(sock,id)

def icmp_response_handler(sock,id):
    while True:
        try:
            recv_packet, addr = sock.recvfrom(1024)
        except socket.timeout as e:
            return False

        # print(recv_packet)
        header = recv_packet[20:28]
        data = recv_packet[29:]
        # print(header)
        icmp_type, code, checksum, recv_id, seq = struct.unpack(pack_format, header)
        # print((icmp_type, checksum, id, seq))
        # validation_header = struct.pack(pack_format, icmp_type, code, 0, recv_id, seq)
        # validation_checksum = get_checksum(validation_header+data)
        #if checksum != validation_checksum:
        #    print((checksum, validation_checksum))
        #    raise BADChecksum('Unmatching checksums : %s and %s' % (checksum, validation_checksum))
        #elif id == recv_id:
        # print('--------validation--------')
        if icmp_type == 0:
            if id == recv_id:
                # print('ok')
                return True
            else:
                print('badwolf')






