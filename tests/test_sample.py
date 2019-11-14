# This script serves to be run as a test to make sure circleci setup is OK
from __future__ import print_function, absolute_import, division

def incr(x):
    return x + 1


def test_itworks():
    assert incr(1) == 2
