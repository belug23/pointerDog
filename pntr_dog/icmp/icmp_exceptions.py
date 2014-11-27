"""Defined exceptions for the icmp module"""


class BadOSUserException(Exception):
    def __init__(self, value):
        self.value = "The current user is not : %s" % value
    def __str__(self):
        return repr(self.value)

