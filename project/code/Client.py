from __future__ import division

from random import random, randint


class Client:
    WT_MIN = 0
    WT_MAX = 5

    def __init__(self, id, req):
        self.id = id
        self.weight = int(self.WT_MIN + random() * (self.WT_MAX - self.WT_MIN))
        self.importance = [randint(0,5)]*(req)