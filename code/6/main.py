from __future__ import print_function
import random


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


class Osyczka2(Model):
    pass


class Kursawe(Model):
    pass


class Schaffer(Model):
    _max = float("-inf")
    _min = float("inf")

    def __init__(self):
        Schaffer._set_max_min()
        decisions = [Decision('x', high=Schaffer._max, low=Schaffer._min)]
        objectives = [Objective('y')]
        super(Schaffer, self).__init__(n_des=1, n_obj=1, decisions=decisions, objectives=objectives)

    @staticmethod
    def _set_max_min(self):
        """Calculate the maximum and minimum of (F1 + F2)

            A baseline study where you run the Schaffer 10000 times to find the min
            and max values for (f1 + f2). This is needed to normalize the shaffer
            objective function value in 0..1.
        """
        def find_max_f1_f2(x):
            return pow(x, 2) + pow(x - 2, 2)
        for i in range(10000):
            e = find_max_f1_f2(random.randint(-100000, 100000))
            Schaffer._max = e if e > Schaffer._max else Schaffer._max
            Schaffer._min = e if e < Schaffer._min else Schaffer._min

    def any(self):
        return self.decisions[0].generate_one()

    def evaluate(self, x):
        return (pow(x, 2) + pow((x - 2), 2) - Schaffer._min) / float(Schaffer._max - Schaffer._min)


def simulated_annealing(model):
    print("\nNote: ")
    print("Each line represents a cycle of {0} trials. \nEach trial is represented by a full stop i.e. '.'".format(m))
    print("Additionally: \n'?' means we picked a state that was not as good as the present state. i.e 'A drunken decision'")
    print("'+' means we picked a state that was better than the current one.")
    print("'!' means we picked a state that is the best among the states encounterd yet.")
    print("For larger n and m, the number of ? printed should decrease.")
    n = 500
    m = 50
    mod = model()
    K_MAX = 1000
    random.seed(1)  # TODO : Activate this line only when Debugging
    best_state = cur_state = mod.any()
    best_energy = cur_energy = mod.evaluate(cur_state)
    print("Initial State: {0}\nInitial Energy: {1} \n".format(cur_state, cur_energy))
    k = 1
    for i in range(n):
        print()
        print(', {0}, :{1:.2f},\t'.format(m * i, best_energy), end="")
        for j in range(m):
            next_state = mod.any()
            next_energy = mod.evaluate(next_state)
            if next_energy < best_energy: # TODO: make this comparasion test more general
    pass


def max_walk_sat():
    pass


if __name__ == '__main__':
    for model in [Schaffer, Osyczka2, Kursawe]:
        for optimizer in [simulated_annealing, max_walk_sat]:
            optimizer(model())