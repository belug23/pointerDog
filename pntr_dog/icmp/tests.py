import struct
import sys

from django.test import TestCase

from . import icmp_lib


class IcmpTestCase(TestCase):
#    def setUp(self):
#        self.config = testing.setUp()

 #   def tearDown(self):
 #       testing.tearDown()

    def assertIsPacket(self, packet, sent_id=1):
        #8byte header + 32byte data
        self.assertEqual(len(packet), 40)
        #unpack the header to test it
        header = packet[:-32]
        packet_type, code, checksum, recived_id, seq = struct.unpack('bbHHh', header)
        self.assertEqual(packet_type,8)
        self.assertEqual(code,0)
        self.assertEqual(recived_id, sent_id)


    def test_checksum(self):
        #build header and data
        test_data = b'\x00\x01\xf2\x03\xf4\xf5\xf6\xf7' #Data from RFC 1071
        #Get checksum
        checksum = icmp_lib.get_checksum(test_data)
        #Compare with valid checksum
        self.assertEqual(checksum, 0xddf2)

    def test_packet_creation(self):
        #create a packet
        packet = icmp_lib.get_packet(1)
        #validate the return result to be valid
        self.assertIsPacket(packet)


    def test__checksum_corrupted_data(self):
        #build header and data
        test_data = b'\x00\x01\xf2\x03\xf4\xf5\xf6\xf7' #Data from RFC 1071
        #Get checksum
        checksum = icmp_lib.get_checksum(test_data)
        #Change 1 bit of data from the header (Corruption)
        test_data = b'\x00\x01\xf2\x00\xf4\xf5\xf6\xf7' #Corrupted byte 4 from \x03 to \x00
        #Get Checksum
        checksum_corrupted = icmp_lib.get_checksum(test_data)
        #Response should be different from the first checksum
        self.assertNotEqual(checksum, checksum_corrupted)

    def test_icmp_send(self):
        #Call a ICMP test on localhost
        is_alive = icmp_lib.icmp_call('127.0.0.1')
        #Check if it succedded
        self.assertTrue(is_alive)

    def test_icmp_fail(self):
        #Find a not responding IP address
        is_alive = icmp_lib.icmp_call('10.255.255.254')
        #Make certain that it fail correcttly
        self.assertFalse(False)
