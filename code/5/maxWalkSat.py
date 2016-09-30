from __future__ import print_function

import copy
import pdb
import random
import matplotlib.pyplot as plt


def find_osyczka_max_min():
    def calculate_energy(f1, f2):
        return f1 + f2
    prob = Problem()
    _max = -float('inf')
    _min = float('inf')
    for i in range(1000):
        state = prob.generate_one()  # Will generate a valid state
        objectives = prob.evaluate_objective(state)
        state_energy = calculate_energy(objectives['f1'], objectives['f2'])
        _max = state_energy if state_energy > _max else _max
        _min = state_energy if state_energy < _min else _min
    return _max, _min


def osyczka_energy(state):
    f1 = state.objectives['f1']
    f2 = state.objectives['f2']
    return (f1 + f2 - OSZ_MIN) / float(OSZ_MAX + OSZ_MIN)


def f1_osyczka2(x1, x2, x3, x4, x5, x6):
    """ f1(x) = -(25 * (x1 - 2)^2 + (x2-2)^2 + (x3-1)^2(x4-4)^2 + (x5-1)^2)"""
    return -1 * ((25 * pow(x1 - 2, 2)) +
                 pow((x2 - 2), 2) +
                 pow(x3 - 1, 2) * pow(x4 - 4, 2) +
                 pow(x5 - 1, 2))


def f2_osyczka2(x1, x2, x3, x4, x5, x6):
    """ f2(x) = x1**2 + x2**2 + x3**2 + x4**2 + x5**5 + x6**6 """
    return x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 + x5 ** 2 + x6 ** 2


class O(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Decision(O):
    def __init__(self, name, low, high):
        O.__init__(self, name=name, low=low, high=high)
        # super(Decision, self).__init__(name=name, low=low, high=high)


class Objective(O):
    def __init__(self, name):
        O.__init__(self, name=name, do_minimize=True)


class State:
    def __init__(self, x1, x2, x3, x4, x5, x6):
        self.decisions = dict(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6)
        self.objectives = dict()

    def clone(self):
        new_variable = State(**self.decisions)
        new_variable.objectives = self.objectives
        return new_variable


class Problem(O):
    def __init__(self):
        O.__init__(self)
        self.decisions = [Decision('x1', 0, 10), Decision('x2', 0, 10),
                          Decision('x3', 1, 5), Decision('x4', 0, 6),
                          Decision('x5', 1, 5), Decision('x6', 0, 10)]
        self.objectives = [Objective('f1'), Objective('f2')]

    @staticmethod
    def evaluate_objective(state):

        # def f1():
        #     return -(25 * pow(d['x1'] - 2, 2) + pow(d['x2'] - 2, 2) + pow(d['x3']-1, 2) * pow(d['x4'] - 4, 2) +
        #              pow(d['x5'] - 1, 2))
        #
        # def f2():
        #     return d['x1'] ** 2 + d['x2'] ** 2 + d['x3'] ** 2 + d['x4'] ** 2 + d['x5'] ** 2 + d['x6'] ** 2

        f1 = f1_osyczka2(**state.decisions)
        f2 = f2_osyczka2(**state.decisions)
        state.objectives = {'f1': f1, 'f2': f2}
        return state.objectives

    @staticmethod
    def is_valid(state):
        def _is_valid(x1, x2, x3, x4, x5, x6):
            try:
                assert 0 <= x1 + x2 - 2
                assert 0 <= 6 - x1 - x2
                assert 0 <= 2 - x2 + x1
                assert 0 <= 2 - x1 + 3 * x2
                assert 0 <= 4 - pow((x3 - 3), 2) - x4
                assert 0 <= pow(x5 - 3, 2) + x6 - 4
                return True
            except AssertionError:
                return False

        return _is_valid(**state.decisions)

    def generate_one(self):
        i = 0
        max_retries = 1000  # # Try to find a valid state for max_tries number of times at max
        while True and i < max_retries:
            variables = {}
            for dec in self.decisions:
                variables[dec.name] = random.randint(dec.low, dec.high)
            state = State(**variables)
            #pdb.set_trace()
            if Problem.is_valid(state=state):
                return state
            i += 1
        if i >= max_retries:
            raise Exception("Could not generate a valid point in {} number of retries".format(max_retries))


OSZ_MAX, OSZ_MIN = find_osyczka_max_min()
print("OSZ_MIN = {0} , OSZ_MAX = {1}".format(OSZ_MIN, OSZ_MAX))


def energy(state):
    return (state.objectives['f1'] + state.objectives['f2'] - OSZ_MIN) / float(OSZ_MAX - OSZ_MIN)

P = 0.5
MAX_TRIES = 100
MAX_CHANGES = 50
# Rather than breaking when score(solution) > threshold, we will try to see how good the solution gets

my_data = []
def max_walk_sat():
    global z
    prob = Problem()
    state_best = prob.generate_one()
    prob.evaluate_objective(state_best)
    energy_best = energy(state_best)
    my_data.append(energy_best)
    for i in range(MAX_TRIES):  # FOR i = 1 to max-tries DO
        state_random = prob.generate_one()  # solution = random assignment
        prob.evaluate_objective(state_random)
        # energy_random = energy(state_random)

        for j in range(MAX_CHANGES):  # FOR j =1 to max-changes DO
            rand_decision = random.choice(prob.decisions)  # Pick at random on which decision to change # c = random part of solution
            state_new = copy.deepcopy(state_random)
            if P < random.random():  # IF    p < random()
                # change a random setting in c
                state_new.decisions[rand_decision.name] = random.randint(rand_decision.low, rand_decision.high)
                if prob.is_valid(state_new):
                    prob.evaluate_objective(state_new)
                    energy_new = energy(state_new)

                    # energy_best = max(energy_new, energy_best)
                    if energy_new > energy_best:
                        print ("!", end="")
                        energy_best = energy_new
                        state_best = state_new
                        my_data.append(energy_best)
            else:
                # change setting in c that maximizes score(solution)
                for m in range(rand_decision.low, rand_decision.high):
                    state_new.decisions[rand_decision.name] = random.randint(rand_decision.low, rand_decision.high)
                    if prob.is_valid(state_new):
                        energy_new = energy(state_new)
                        if energy_new > energy_best:
                            print("+", end="")
                            energy_best = energy_new
                            state_best = state_new
                            my_data.append(energy_best)

        print (".")
    return my_data, state_best


def plot_point(my_data):
    plt.plot(range(len(my_data)), my_data, "o")
    plt.show()

my_data, my_state = max_walk_sat()
print ("{0} {1}".format(my_state.decisions, my_data[-1]))
plot_point(my_data)
"""
FOR i = 1 to max-tries DO
  solution = random assignment
  FOR j =1 to max-changes DO
    IF  score(solution) > threshold
        THEN  RETURN solution
    FI
    c = random part of solution
    IF    p < random()
    THEN  change a random setting in c
    ELSE  change setting in c that maximizes score(solution)
    FI
RETURN failure, best solution found
"""
