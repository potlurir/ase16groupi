from __future__ import print_function
from __future__ import division


class Decision(object):
    def __init__(self, name, high, low):
        self.name = name
        self.low = low
        self.high = high


class Objective(object):
    def __init__(self, name, do_minimize=True):
        self.name = name
        self.do_minimize = do_minimize


class NRP(object):
    def __init__(self, n_requirements, n_releases, n_clients, density, budget):
        pass

    def generate_random_data(self):
        # Creates imaginary random clients, requirements and clients value for a requiremnt
        pass

    def check_buget_constraint(self):
        # Checks if the requiremnts selected don't exceed the budget
        pass

    def check_requirement_dependency(self):
        # Checks if the dependency among the requirements is satisfied
        pass

    def evaluate(self, decisions):
        pass
    