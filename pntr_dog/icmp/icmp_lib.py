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
    # print(ip_addr)
    icmp = socket.getprotobyname("icmp")
    id = os.getpid() & 0xFFFF
    packet = get_packet(id)
    if os.getuid() == 0:
        # if root do the perfect ping
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    else:
        raise BadOSUserException('Root')
    sock.settimeout(3)
    while packet:
        chunk_size = sock.sendto(packet,(ip_addr, 7))
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
        validation_header = struct.pack(pack_format, icmp_type, code, 0, recv_id, seq)
        validation_checksum = get_checksum(validation_header+data)
        #if checksum != validation_checksum:
        #    print((checksum, validation_checksum))
        #    raise BADChecksum('Unmatching checksums : %s and %s' % (checksum, validation_checksum))
        #elif id == recv_id:
        # print('--------validation--------')
        if id == recv_id:
            print('ok')
            return True






