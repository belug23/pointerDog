import unittest

from pyramid import testing

from pntr_dog.icmp import icmp_lib, IcmpController


class IcmpLibTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_checksum(self):
        #build header and data
        #Get checksum
        #Compare with valid checksum
        self.assertTrue(False)

    def test_packet_creation(self):
        #create a packet
        #validate the return result to be valid
        self.assertTrue(False)

    def test__checksum_corrupted_data(self):
        #build header and data
        #Get checksum
        #Change 1 bit of data from the header (Corruption)
        #Get Checksum
        #Response should be different from the first checksum
        self.assertTrue(False)

    def test_icmp_send(self):
        #Call a ICMP test on localhost
        #Check if it succedded
        self.assertTrue(False)

    def test_icmp_fail(self):
        #Find a not responding IP address
        #Make certain that it fail correcttly
        self.assertTrue(False)


class IcmpContollerTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        #Add server in database
        #Add server in the database
        #Configure it to make it alert at first fail
        #Add server in the database
        #Configure it to make it alert at third fail

    def tearDown(self):
        testing.tearDown()

    def test_icmp_controller_success(self):
        #Override icmp.test to return "True" see : http://stackoverflow.com/questions/14956825/python-unit-testing-code-which-calls-os-module-level-python-functions
        #Run the ICMP call of the controller on the server
        #Does the data in the database is return ok
        #Does the respond is ok
        self.assertTrue(False)

    def test_icmp_controller_alert_on_first_fail(self):
        #Override icmp.test to return "False" see : http://stackoverflow.com/questions/14956825/python-unit-testing-code-which-calls-os-module-level-python-functions
        #Run the ICMP call from the controller
        #make if fail
        #Does the alert is sent
        #Using mock to check if it's called see : http://stackoverflow.com/questions/18762293/how-to-test-that-a-function-is-called-within-a-function-with-nosetests
        #Does the respond is ok
        self.assertTrue(False)

    def test_icmp_controller_alert_on_multiple_fail(self):
        #Override icmp.test to return "False" see : http://stackoverflow.com/questions/14956825/python-unit-testing-code-which-calls-os-module-level-python-functions
        #Run the ICMP call from the controller
        #make if fail
        #Does the alert is not sent
        #Using mock to check if it's called see : http://stackoverflow.com/questions/18762293/how-to-test-that-a-function-is-called-within-a-function-with-nosetests
        #Does the respond is ok
        #Repeat 3 times
        #At the third time is the alert sent?
        #Using mock to check if it's called see : http://stackoverflow.com/questions/18762293/how-to-test-that-a-function-is-called-within-a-function-with-nosetests
        self.assertTrue(False)

    def test_icmp_controller_get_test_list(self):
        #Get the list of servers
        #Make sure it's good
        self.assertTrue(False)

