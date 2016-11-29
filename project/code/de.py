import os
import pdb
import sys
import threading

sys.path.append(os.path.abspath('.'))
from matplotlib import pyplot as plt
from copy import deepcopy
import random
from math import exp
from nrp import NRP, State


def _xor(arr1, arr2):
    return [x^y for x, y in zip(arr1, arr2)]


def _union(arr1, arr2):
    return [x or y for x,  y in zip(arr1, arr2)]


def _intersection(arr1, arr2):
    return [x and y for x, y in zip(arr1, arr2)]


def _is_continous_dominated(C, T, limits):
    # Returns True if T dominates C.
    # from https://github.com/ai-se/softgoals/blob/master/src/utilities/de.py#L141
    #pdb.set_trace()

    def normalize(val, _max, _min):
        # Let's see if this ever generates divide by zero exception.
        _max = max(_max, val)
        _min = min(_min, val)
        _max += 0.0001 if _max == _min else 0  # TO handle Divide by Zero
        return (val - _min)/float(_max - _min)

    def exp_loss(c, t, w, n):
        return -1 * exp(w * ( c - t)/float(n))

    def loss(c, t):
        c_norm = [normalize(val, limit[0], limit[1]) for val, limit in zip(c.objectives, limits)]
        t_norm = [normalize(val, limit[0], limit[1]) for val, limit in zip(t.objectives, limits)]
        n = len(c.objectives)
        losses = [exp_loss(c,t,w,n) for c, t, w in zip(c_norm, t_norm, [1, 1])]
        return sum(losses)/float(n)

    l1 = loss(C, T)  # l1 is loss associated with picking C over T
    l2 = loss(T, C)  # l2 is loss accociated with picking T over C
    return l2 < l1  # Return true if the loss associated with picking T is less


def _is_binary_dominated(C, T, limits=None):
    # Return true if C is dominated by T.
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


class DifferentialEvolution(object):

    def __init__(self, model=NRP, population_size=40, f=0.3):
        assert population_size > 0
        assert 0.0 < f < 1.0
        self.model = model(n_requirements=50, budget=2000)
        self.population_size = population_size
        self.f = f

        self.population = set()

    def generate_population(self):
        """Generates and evaluates a population of random candidates"""
        while len(self.population) < self.population_size:
            candidate = self.model.any()
            if candidate not in self.population:
                self.population.add(candidate)
                self.model.evaluate(candidate)
            else:
                print("Duplicate Candidate Generated")

    def pareto_frontier_candidates(self, population=None):
        """Compares each candidate with the rest of population using BDOM
        and reports the ones that were never dominated.
        if population is None then reports the pareto frontier of self.population"""
        population = deepcopy(self.population) if population is None else population
        population = list(population)
        for can in population:
            for can1 in population:
                if _is_binary_dominated(can1, can):
                    population.remove(can1)
        for can in population:
            for can1 in population:
                if _is_binary_dominated(can1, can):
                    population.remove(can1)
        return set(population)

    def prune_population(self, iterations=None):
        """Picks and compares (using BDOM) two distinct candidates at random
        and kills the one that was dominated.
        Note: This changes the population size"""
        iterations = self.population_size * 2 if iterations is None else iterations
        assert iterations > 0
        for _ in xrange(iterations):
            A, B = random.sample(self.population)
            if _is_binary_dominated(A, B):  # If A is dominated by B
                self.population.remove(A)
            elif _is_binary_dominated(B, A):
                self.population.remove(B)

    def any3(self, population=None):
        """Picks 3 candidates from the population"""
        population = self.population if population is None else population
        smp = random.sample(population, 3)
        return smp

    def get_min_max_of_objectives(self):
        # Find the max and min of objectives in population
        obj1 = [candidate.objectives.cost for candidate in self.population]
        obj2 = [candidate.objectives.satisfaction for candidate in self.population]
        cost_max = max(obj1)
        cost_min = min(obj1)
        sat_max = max(obj2)
        sat_min = min(obj2)
        print("cost_max, cost_min, sat_max, sat_min")
        print(cost_max, cost_min, sat_max, sat_min)
        return ((cost_max, cost_min), (sat_max, sat_min))

    def run_de(self, iterations=2000, comparator=_is_continous_dominated):
        """
        Returns a new set of candidates, keeps the population of class unchanged
        Keeps the population unchanged
        For x number of iterations:
        Pick 3 members (A, B, C) at random
        T = C  + F * ( B - C)
        If T is a valid mutant.
            if T is better than C:
                Replace C in population by T
        :return modified population
        """
        population = deepcopy(self.population)
        limits = self.get_min_max_of_objectives()
        for _ in xrange(iterations):
            if len(population) < 3:
                break
            A, B, C = self.any3(population)
            F = [0 if self.f > random.random() else -1 for _ in range(len(A.decisions))]
            # DE/rand/1.  For binary operators. T = (A OR (F AND( B XOR C )))
            T = _union(A.decisions, _intersection(F, _xor(B.decisions, C.decisions)))
            T = State(T)
            objectives = self.model.evaluate(T)
            if objectives is None:
                print ("The mutant was not acceptable")
                continue
            if comparator(C, T, limits):  # If C is dominated by T
                population.remove(C)
                if T in population:
                    pass
                    #print("Duplicate mutant candidate generated")
                else:
                    population.add(T)
        return population


#
# def differential_evolution(model_=NRP, population_size=40, f=0.3):
#     # model = model_()
#     # population = list()
#     # while len(population) < population_size:
#     #     candidate = model.any()
#     #     if candidate not in population:
#     #         # We have to generate distinct population
#     #         population.append(candidate)
#     #     else:
#     #         print("Duplicate found")
#     #
#     # for candidate in population:
#     #     model.evaluate(candidate)
#     #
#     # cost_max = sat_max = float('-inf')
#     # cost_min = sat_min = float('inf')
#     # for candidate in population:
#     #     if candidate.objectives.cost < cost_min:
#     #         cost_min = candidate.objectives.cost
#     #     if candidate.objectives.cost > cost_max:
#     #         cost_max = candidate.objectives.cost
#     #     if candidate.objectives.satisfaction < sat_min:
#     #         sat_min = candidate.objectives.satisfaction
#     #     if candidate.objectives.satisfaction > sat_max:
#     #         sat_max = candidate.objectives.satisfaction
#     # print(cost_max, cost_min, sat_max, sat_min)
#     # limits = [[cost_max, cost_min], [sat_max, sat_min]]
#     # reduce population size. Reject bad candidates
#     # Pick two candidates at random, and kill the one that is dominated.
#     # for _ in range(population_size * 2):
#
#     #     xyz = len(population)-1
#     #     #print(xyz)
#     #     a, b = [random.randint(0, xyz) for _ in range(2)]
#     #     #print(a,b)
#     #     if _is_binary_dominated(population[a], population[b]):
#     #         population.pop(a)
#     #     elif _is_binary_dominated(population[b], population[a]):
#     #         #pdb.set_trace()
#     #         population.pop(b)
    #
    # print ('Initial population size = {0}'.format(len(population)))
    # plot_graph(population, None)
    # initial_population = deepcopy(population)
    # new_candidates = []
    # for _ in range(2000):
    #     # while 1:
    #     #     a,b,c = [random.randint(0, len(population)-1) for _ in range(3)]
    #     #     #print('a = {0} b = {1} c = {2}'.format(a, b, c))
    #     #     if a != b and a != c and b != c:
    #     #         # We got 3 unique person from the population.
    #     #         break
    #     # A, B, C = [population[i] for i in [a, b, c]]
    #
    #     # assert A in population
    #     # assert B in population
    #     # assert C in population
    #     F = [0 if f > random.random() else -1 for _ in range(len(A.decisions))]
    #     # T = A + f(B-C)  DE/rand/1
    #     # For binary operators,
    #     # T = (A or (F and( B xor C )))
    #     T = _union(A.decisions, _intersection(F, _xor(B.decisions, C.decisions)))
    #     T = State(T)
    #     objectives = model.evaluate(T)
    #
    #     if objectives is not None:
    #         if _is_continous_dominated(C, T, limits):  # If C is dominated by T
    #         # if _is_binary_dominated(C, T): # If C is dominated by T
                #print("T.objectives = {0}".format(T.objectives))
                #print("C.objectives = {0}".format(C.objectives))
    #             new_candidates.append(deepcopy(T))
    #
    #             #print (" C was replaced by T")
    #             population[c] = T
    #     else:
    #         print("The mutant was not acceptable")
    # # pdb.set_trace()
    # for can in new_candidates:
    #     for can1 in new_candidates:
    #         if _is_binary_dominated(can1, can):
    #             new_candidates.remove(can1)
    # for can in new_candidates:
    #     for can1 in new_candidates:
    #         if _is_binary_dominated(can1, can):
    #             new_candidates.remove(can1)
    #
    # return new_candidates, None


def plot_graph(population, ini_pop):
    x = list()
    y = list()
    if population is not None:
        for candidate in population:
            x.append(candidate.objectives[0])
            y.append(candidate.objectives[1])
        plt.plot(x, y, '.')

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
    de = DifferentialEvolution(population_size=300)
    de.generate_population()
    pareto = de.pareto_frontier_candidates()
    optimized = de.run_de()
    op_pareto = de.pareto_frontier_candidates(optimized)
    plot_graph(de.population, pareto)
    plot_graph(optimized, op_pareto)
