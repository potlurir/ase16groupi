
from __future__ import print_function
import pdb
from matplotlib import pyplot as plt
from copy import deepcopy
import random
from ..NRP.nrp import NRP
from ..NRP.nrp import State


def _xor(arr1, arr2):
    return [x^y for x,y in zip(arr1, arr2)]


def _union(arr1, arr2):
    return [x or y for x,y in zip(arr1, arr2)]


def _intersection(arr1, arr2):
    return [x and y for x,y in zip(arr1, arr2)]


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
    while len(population) < population_size:
        candidate = model.any()
        if candidate not in population:
        #if True:  # We have to generate distinct population
            population.append(candidate)
        else:
            print("Duplicate found")

    for candidate in population:
        model.evaluate(candidate)

    # reduce population size. Reject shitty candidates
    # Pick two candidates at random, and kill the one that is dominated.
    # for _ in range(population_size):
    #
    #     xyz = len(population)-1
    #     print(xyz)
    #     a, b = [random.randint(0, xyz) for _ in range(2)]
    #     print(a,b)
    #     if _is_binary_dominated(population[a], population[b]):
    #         population.pop(a)
    #     elif _is_binary_dominated(population[b], population[a]):
    #         #pdb.set_trace()
    #         population.pop(b)

    print ('Initial population size = {0}'.format(len(population)))
    plot_graph(population, None)
    #initial_population = deepcopy(population)
    # We need 3 unique person from the population.
    # TODO: But I will care about that later
    new_candidates = []
    for _ in range(5000):  # It should be n_decision * 10.
        while 1:
            a,b,c = [random.randint(0, len(population)-1) for _ in range(3)]
            #print('a = {0} b = {1} c = {2}'.format(a, b, c))
            if a != b and a != c and b != c:
                break
        A, B, C = [population[i] for i in [a, b, c]]
        assert A in population
        assert B in population
        assert C in population
        F = [f > random.random() for _ in range(len(A.decisions))]
        # T = A + f(B-C)  DE/rand/1
        # For binary operators,
        # T = (A or (F and( B xor C )))
        T = _union(A.decisions, _intersection(F, _xor(B.decisions, C.decisions)))
        T = State(T)
        objectives = model.evaluate(T)

        if objectives is not None:
            if _is_binary_dominated(C, T): # If C is dominated by T
                print("T.objectives = {0}".format(T.objectives))
                print("C.objectives = {0}".format(C.objectives))
                new_candidates.append(deepcopy(T))
                #replaced_population.append(deepcopy(C))

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
    new_candidates, population = differential_evolution(population_size=300, f=0.2)
    print (len(new_candidates))

    plot_graph(new_candidates, population)
