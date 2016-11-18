
from __future__ import print_function
import pdb
from matplotlib import pyplot as plt
from copy import deepcopy
import random
from math import exp
from ..NRP.nrp import NRP
from ..NRP.nrp import State


def _xor(arr1, arr2):
    return [x^y for x,y in zip(arr1, arr2)]


def _union(arr1, arr2):
    return [x or y for x,y in zip(arr1, arr2)]


def _intersection(arr1, arr2):
    return [x and y for x,y in zip(arr1, arr2)]
"""
def cdom(self, obj1, obj2):

    Continuous Domination
    :param obj1: Objective 1
    :param obj2: Objective 2
    :return: Check if objective 1 dominates objective 2 based on exponential loss.

    def norm(val, least, most):
      least = min(least, val)
      most = max(most, val)
      return (val - least) / (most - least + 0.0001)
    def exp_loss(x_i, y_i, w_i, n):
      return -1*exp(w_i*(x_i-y_i)/n)
    def loss(x, y):
      x_norm = [norm(v,lo,hi) for v,lo,hi in zip(x, self.limits.mins, self.limits.maxs)]
      y_norm = [norm(v,lo,hi) for v,lo,hi in zip(y, self.limits.mins, self.limits.maxs)]
      n = len(x)
      losses = [exp_loss(x_i, y_i, w_i, n) for x_i, y_i, w_i in zip(x_norm, y_norm, self.limits.weights)]
      return sum(losses)/n
    l1 = loss(obj1, obj2)
    l2 = loss(obj2, obj1)
return abs(l1 - l2) > self.settings.cdom_delta and l1 < l2"""

def _is_continous_dominated(C, T, limits):
    # Returns True if T dominates C.
    #pdb.set_trace()

    def normalize(val, _max, _min):
        # TODO: divide by zero
        # Let's see if this ever generates divide by zero exception.
        _max = max(_max, val)
        _min = min(_min, val)
        return (val - _min)/float(_max - _min)

    def exp_loss(c, t, w, n):
        return -1 * exp(w * ( c - t)/float(n))

    def loss(c, t):
        c_norm = [normalize(val, limit[0], limit[1]) for val, limit in zip(c.objectives, limits)]
        t_norm = [normalize(val, limit[0], limit[1]) for val, limit in zip(t.objectives, limits)]
        n = len(c.objectives)
        losses = [exp_loss(c,t,w,n) for c, t, w in zip(c_norm, t_norm, [-1, 1])]
        return sum(losses)/float(n)

    l1 = loss(C, T)  # l1 is loss associated with picking C over T
    l2 = loss(T, C)  # l2 is loss accociated with picking T over C
    return l2 < l1  # Return true if the loss associated with picking T is less
    # cst = (T.objectives.cost - C.objectives.cost)/float(cost_normalizer)
    # sat = (T.objectives.satisfaction - C.objectives.satisfaction) / float(sat_normalizer)





def _is_binary_dominated(C, T):
    # Check if T dominates C
    # C and T are states
    dominated = False
    try:
        for obj1, obj2 in zip(C.objectives, T.objectives):
            assert obj1 <= obj2
            if obj1 < obj2:
                dominated = True
    except AssertionError:
        return False
    # if C.objectives[1] < T.objectives[1]: # Just checking on satisfaction.
    #     dominated = True
    return dominated


def differential_evolution(model_=NRP, population_size=40, f=0.3):
    model = model_()
    # This might raise an exception
    population = list()
    while len(population)  < population_size:
        candidate = model.any()
        if candidate not in population:
            # We have to generate distinct population
            population.append(candidate)
        else:
            print("Duplicate found")

    for candidate in population:
        model.evaluate(candidate)

    cost_max = sat_max = float('-inf')
    cost_min = sat_min = float('inf')
    for candidate in population:
        if candidate.objectives.cost < cost_min:
            cost_min = candidate.objectives.cost
        if candidate.objectives.cost > cost_max:
            cost_max = candidate.objectives.cost
        if candidate.objectives.satisfaction < sat_min:
            sat_min = candidate.objectives.satisfaction
        if candidate.objectives.satisfaction > sat_max:
            sat_max = candidate.objectives.satisfaction
    print(cost_max, cost_min, sat_max, sat_min)
    limits = [[cost_max, cost_min], [sat_max, sat_min]]
    # reduce population size. Reject bad candidates
    # Pick two candidates at random, and kill the one that is dominated.
    # for _ in range(population_size * 2):
    #
    #     xyz = len(population)-1
    #     #print(xyz)
    #     a, b = [random.randint(0, xyz) for _ in range(2)]
    #     #print(a,b)
    #     if _is_binary_dominated(population[a], population[b]):
    #         population.pop(a)
    #     elif _is_binary_dominated(population[b], population[a]):
    #         #pdb.set_trace()
    #         population.pop(b)

    print ('Initial population size = {0}'.format(len(population)))
    #plot_graph(population, None)
    #initial_population = deepcopy(population)
    new_candidates = []
    for _ in range(500):
        while 1:
            a,b,c = [random.randint(0, len(population)-1) for _ in range(3)]
            #print('a = {0} b = {1} c = {2}'.format(a, b, c))
            if a != b and a != c and b != c:
                # We got 3 unique person from the population.
                break
        A, B, C = [population[i] for i in [a, b, c]]

        # assert A in population
        # assert B in population
        # assert C in population
        # TODO:
        F = [0 if f > random.random() else -1 for _ in range(len(A.decisions))]
        #pdb.set_trace()
        # T = A + f(B-C)  DE/rand/1
        # For binary operators,
        # T = (A or (F and( B xor C )))
        T = _union(A.decisions, _intersection(F, _xor(B.decisions, C.decisions)))
        T = State(T)
        objectives = model.evaluate(T)

        if objectives is not None:
            if _is_continous_dominated(C, T, limits):  # If C is dominated by T
            # if _is_binary_dominated(C, T): # If C is dominated by T
                print("T.objectives = {0}".format(T.objectives))
                print("C.objectives = {0}".format(C.objectives))
                new_candidates.append(deepcopy(T))

                print (" C was replaced by T")
                population[c] = T
        else:
            print("The mutant was not acceptable")

    return new_candidates, population


def plot_graph(ini_pop, population, marker='.'):
    x = list()
    y = list()
    if population is not None:
        for candidate in population:
            x.append(candidate.objectives[0])
            y.append(candidate.objectives[1])
        plt.plot(x, y, marker)

    if ini_pop is not None:
        a = list()
        b = list()
        for candidate in ini_pop:
            a.append(candidate.objectives[0])
            b.append(candidate.objectives[1])
        plt.plot(a,b, 'o')

    plt.xlabel('cost ->')
    plt.ylabel('satisfaction ->')
    plt.show()

if __name__ == '__main__':
    random.seed(1)
    xyz = []
    # for i in range(4):
    #     new_candidates, population = differential_evolution(population_size=300, f=0.05 * i)
    #     xyz.append(len(new_candidates))
    # print(xyz)
    new_candidates, population = differential_evolution(population_size=300, f=0.8)
    print (len(new_candidates))

    plot_graph(new_candidates, population)
