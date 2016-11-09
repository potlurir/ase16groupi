from __future__ import division

from random import random


class Requirement:
    RISK_MIN = 1
    RISK_MAX = 5
    COST_MIN = 10
    COST_MAX = 20

    def __init__(self, id):
        self.id = id
        self.risk = int(self.RISK_MIN + random() * (self.RISK_MAX - self.RISK_MIN))
        self.cost = int(self.COST_MIN + random() * (self.COST_MAX - self.COST_MIN))