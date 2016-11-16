from __future__ import print_function

from ..NRP.nrp import NRP
from ..NRP.nrp import State
import random


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
    return dominated

def differential_evolution(model_=NRP, population_size=40, f=0.8):
    model = model_()
    # This might raise an exception
    population = [model.any() for _ in range(population_size)]
    for candidate in population:
        model.evaluate(candidate)
    # We need 3 unique person from the population.
    # TODO: But I will care about that later
    for _ in range(200):
        a,b,c = [random.randint(0, population_size-1) for _ in range(3)]
        A, B, C = [population[i] for i in [a,b,c]]
        F = [f > random.random() for _ in range(len(A.decisions))]
        # T = A + f(B-C)  DE/rand/1
        # For binary operators,
        # T = (A or (F and( B xor C )))
        T = _union(A.decisions, _intersection(F, _xor(B.decisions, C.decisions)))
        T = State(T)
        objectives = model.evaluate(T)
        if objectives is not None:
            if _is_binary_dominated(C, T): # If C is dominated by T
                population[c] = T
        else:
            print("The mutant was not acceptable")

    return population

if __name__ == '__main__':
    population = differential_evolution()
    x = list()
    y = list()
    for candidate in population:
        x.append(candidate.objectives[0])
        y.append(candidate.objectives[1])
    from matplotlib import pyplot as plt

    plt.plot(x, y, '.')

    plt.xlabel('cost ->')
    plt.ylabel('satisfaction ->')
    plt.show()