from __future__ import print_function
import utest


@utest.ok
def say_hello(name=None):
    """The first words a programmer says"""
    print("hello {0}".format(name or "world"))


@utest.ok
def must_fail():
    """The world shall end if this passes"""
    assert 'pritesh' == 'ranjan'
