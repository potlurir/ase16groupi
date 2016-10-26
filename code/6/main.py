from __future__ import print_function
from __future__ import division

import random
import math


class Decision(object):
    def __init__(self, name, high, low):
        self.name = name
        self.low = low
        self.high = high

    def generate_one(self):
        return random.randint(self.low, self.high)


class Objective(object):
    def __init__(self, name, do_minimize=True):
        self.name = name
        self.do_minimize = do_minimize


class Model(object):
    def __init__(self, n_des=0, n_obj=0, decisions=None, objectives=None):
        self.n_des = n_des
        self.n_obj = n_obj
        self.decisions = decisions
        self.objectives = objectives

    def is_valid(self, *args): return True

    def evaluate(self, *args): return None

    def any(self, *args): return None


class State(object):
    def __init__(self, **kwargs):
        self.decisions = kwargs
        self.objectives = dict()

    def clone(self):
        new_state = State(**self.decisions)
        new_state.objectives = self.objectives
        return new_state


class Osyczka2(Model):
    def __init__(self):
        decisions = [Decision('x1', low=0, high=10), Decision('x2', low=0, high=10),
                     Decision('x3', low=1, high=5), Decision('x4', low=0, high=6),
                     Decision('x5', low=1, high=5), Decision('x6', low=0, high=10)]
        objectives = [Objective('f1'), Objective('f2')]
        super(Osyczka2, self).__init__(n_des=6, n_obj=2, decisions=decisions, objectives=objectives)

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

    @staticmethod
    def evaluate(state):
        def objective1(x1, x2, x3, x4, x5, x6):
            """ objective1(x) = -(25 * (x1 - 2)^2 + (x2-2)^2 + (x3-1)^2(x4-4)^2 + (x5-1)^2)"""
            return -1 * ((25 * pow(x1 - 2, 2)) +
                         pow((x2 - 2), 2) +
                         pow(x3 - 1, 2) * pow(x4 - 4, 2) +
                         pow(x5 - 1, 2))

        def objective2(x1, x2, x3, x4, x5, x6):
            """ objective2(x) = x1**2 + x2**2 + x3**2 + x4**2 + x5**5 + x6**6 """
            return x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 + x5 ** 2 + x6 ** 2

        f1 = objective1(**state.decisions)
        f2 = objective2(**state.decisions)
        state.objectives = dict(f1=f1, f2=f2)
        return f1, f2

    def any(self, *args):
        """Generate a state, try again if the generated state was not valid"""
        i = 0
        max_retries = 1000
        # Try to find a valid state for max_tries number of times at max
        while True and i < max_retries:
            variables = {}
            for dec in self.decisions:
                variables[dec.name] = dec.generate_one()
            state = State(**variables)
            if Osyczka2.is_valid(state=state):
                return state
            i += 1
        if i >= max_retries:
            raise Exception("Could not generate a valid point in {} number of retries".format(max_retries))


class Schaffer(Model):

    def __init__(self):
        decisions = [Decision('x', high=100000, low= -100000)]
        objectives = [Objective('y')]
        super(Schaffer, self).__init__(n_des=1, n_obj=2, decisions=decisions, objectives=objectives)

    def any(self):
        """Returns a State object"""
        dec = self.decisions[0]
        variable = {}
        variable[dec.name] = dec.generate_one()
        return State(**variable)

    def evaluate(self, state):
        """Calculates and stores the objectives in state and returns the normalized sum of objectives"""
        def objective1(x): return pow(x, 2)

        def objective2(x): return pow((x - 2), 2)

        f1 = objective1(**state.decisions)
        f2 = objective2(**state.decisions)
        state.objectives = dict(f1=f1, f2=f2)
        return f1, f2


class Kursawe(Model):
    def __init__(self):
        decisions = [Decision('x1', low=-5, high=5),
                     Decision('x2', low=-5, high=5),
                     Decision('x3', low=-5, high=5)]
        objectives = [Objective('f1'), Objective('f2')]
        super(Kursawe, self).__init__(n_des=3, n_obj=2, decisions=decisions, objectives=objectives)

    def any(self, *args):
        variables = {}
        for dec in self.decisions:
            variables[dec.name] = dec.generate_one()
        return State(**variables)

    def evaluate(self, state):
        """Calculates and stores the objectives in state and returns the normalized sum of objectives"""
        def objective1(xi):
            return sum([-10 * math.exp(-0.2 * math.sqrt(xi[i]**2 + xi[i+1]**2)) for i in [0,1]])

        def objective2(xi):
            return sum([math.pow(abs(xi[i]), 0.8) + 5 * math.sin(math.pow(xi[i], 3)) for i in [0,1,2]])

        f1 = objective1(state.decisions.values())
        f2 = objective2(state.decisions.values())
        state.objectives = dict(f1=f1, f2=f2)
        return f1, f2


def energy(objs, max_, min_):
    return (sum(objs) - min_) / (max_ - min_)


def normalize(model):
    _max = float('-inf')
    _min = float('inf')
    for _ in range(1000):
        e = sum(model.evaluate(model.any()))
        _max = e if e > _max else _max
        _min = e if e < _min else _min
    model.max = _max
    model.min = _min


def simulated_annealing(model):
    def probability(old, new, k): return math.exp((old-new)/k)
    # TODO: provide some way so that n and m don't have to be hardcoded
    n = 100
    m = 50
    K_MAX = 1000

    """
    Since SA doesn't work well with multi-objective optimizations, we shall combine the different objectives
    of a model to generate the energy.
    Then we normalize the calculated energy over MIN and MAX values for that model.
    QUESTION: How to we know the MIN-MAX values for that model? Do a baseline study by running the model 10000 times
    and find the min and max values for the energy.
    """
    print("\nNote: ")
    print("Each line represents a cycle of {0} trials. \nEach trial is represented by a full stop i.e. '.'".format(m))
    print("'?' means we picked a state that was not as good as the present state. i.e 'A drunken decision'")
    print("'+' means we picked a state that was better than the current one.")
    print("'!' means we picked a state that is the best among the states encountered yet.")
    print("For larger n and m, the number of ? printed should decrease.")
    random.seed(1)  # TODO : Activate this line only when Debugging
    normalize(model)
    best_state = cur_state = model.any()
    best_energy = cur_energy = energy(model.evaluate(cur_state), model.max, model.min)
    print("Initial State: {0}\nInitial Energy: {1} \n".format(cur_state.decisions, cur_energy))
    k = 1
    #pdb.set_trace()
    for i in range(n):
        print()
        print(', {0}, :{1:.2f},\t'.format(m * i, best_energy), end="")
        for j in range(m):
            next_state = model.any()
            next_energy = energy(model.evaluate(next_state), model.max, model.min)
            if next_energy < best_energy: # TODO: make this more generic, maximize and minimize
                # We have got the best yet
                best_state = next_state
                best_energy = next_energy
                print('!', end="")

            if next_energy < cur_energy:  # TODO: make this more generic, maximize and minimize
                cur_energy = next_energy
                # cur_state = next_state
                print("+", end="")

            elif probability(cur_energy, next_energy, k/K_MAX) < random.random():
                cur_energy = next_energy
                # cur_state = next_state
                print("?", end="")
            k += 1
            print(".", end="")
    return best_state, best_energy


def max_walk_sat(model):
    # TODO: Provide some way so that these values don't have to be hardcoded
    p = 0.001
    MAX_TRIES = 50
    MAX_CHANGES = 50

    normalize(model)
    best_state = model.any()
    best_energy = energy(model.evaluate(best_state), model.max, model.min)

    print("Initial State: {0}\nInitial Energy: {1} \n".format(best_state.decisions, best_energy))
    for i in range(MAX_TRIES):
        next_state = model.any()
        next_energy = energy(model.evaluate(next_state), model.max, model.min)
        print(', {0}, :{1:.2f},\t'.format(MAX_CHANGES * i, best_energy), end="")
        for j in range(MAX_CHANGES):
            if p < random.random():
                next_state = model.any()
                next_energy = energy(model.evaluate(next_state), model.max, model.min)
                if next_energy < best_energy:
                    print("!", end="")
                    best_energy = next_energy
                    best_state = next_state
            else:
                rand_desc = model.decisions[random.randint(0,len(model.decisions)-1)]
                for m in range(rand_desc.low, rand_desc.high):
                    new_state = next_state.clone()
                    new_state.decisions[rand_desc.name] = rand_desc.generate_one()
                    if model.is_valid(new_state):
                        new_energy = energy(model.evaluate(new_state), model.max, model.min)
                        if new_energy < best_energy:
                            print ('+', end="")
                            best_energy = new_energy
                            best_state = new_state
            print(".", end="")
        print()
    return best_state, best_energy


if __name__ == '__main__':
    for model in [Schaffer, Osyczka2, Kursawe]:
        for optimizer in [simulated_annealing, max_walk_sat]:
            print('\n\nModel : {0} \t Optimizer = {1}'.format(model.__name__, optimizer.__name__))
            best_state, best_energy = optimizer(model())
            print("\nBest State: \n\tDecisions{0}\n\tObjectives{1} \nBest Energy: {2}".format(
                best_state.decisions, best_state.objectives, best_energy))
