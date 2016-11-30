from __future__ import print_function
import os
import pdb
import sys
import math
import threading
import time

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


def make_reference():
    pass


ga_pareto_candidates = set()
de_pareto_candidates = set()


def eucledian(one, two):
    dist = 0
    for a, b in zip(one.objectives, two.objectives):
        dist += (a - b) ** 2
    return math.sqrt(dist)


def sort_solutions(candidates):
    candidates = sorted(candidates, key=lambda x: x.objectives[0])
    return candidates


def closest(candidate, population):
    min_dist = float('inf')
    closest_point = None
    for can in population:
        dist = eucledian(candidate, can)
        if dist < min_dist:
            min_dist = dist
            closest_point = can
    return min_dist, closest_point


def spread(obtained, ideals):
    s_obtained = sort_solutions(obtained)
    s_ideals = sort_solutions(ideals)
    d_f = closest(s_ideals[0], s_obtained)[0]
    d_l = closest(s_ideals[-1], s_obtained)[0]
    n = len(s_ideals)
    distances = []
    for i in range(len(s_obtained) - 1):
        distances.append(eucledian(s_obtained[i], s_obtained[i + 1]))
    d_bar = sum(distances) / float(len(distances))
    d_sum = sum([abs(d_i - d_bar) for d_i in distances])
    delta = (d_f + d_l + d_sum) / float(d_f + d_l + (n - 1) * d_bar)
    return delta


def igd(obtained, ideals):
    # For each ideal candidate, find the distance to the closest item in obtained items
    # report the average of such distances.
    #pdb.set_trace()
    igd_val = sum([closest(ideal, obtained)[0] for ideal in ideals]) / float(len(ideals))
    return igd_val


class AlgorithmBase(object):
    def __init__(self, model=NRP, population_size=50):
        self.model = None
        self.population_size = 0

        self.population = set()
        self.model = model()
        self.population_size = population_size

        self.population = set()

    def generate_population(self):
        """Generates and evaluates a population of random candidates"""
        while len(self.population) < self.population_size:
            candidate = self.model.any()
            if candidate is None:
                continue
            if candidate not in self.population:
                self.population.add(candidate)
                self.model.evaluate(candidate)
            else:
                #print("Duplicate Candidate Generated")
                pass

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
        return population

    def prune_population(self, population=None, iterations=None):
        """Picks and compares (using BDOM) two distinct candidates at random
        and kills the one that was dominated.
        Note: This changes the population size"""
        population = deepcopy(self.population) if population is None else population
        iterations = self.population_size * 2 if iterations is None else iterations
        assert iterations > 0
        for _ in xrange(iterations):
            A, B = random.sample(population, 2)
            if _is_binary_dominated(A, B, self.limits):  # If A is dominated by B
                population.remove(A)
            elif _is_binary_dominated(B, A):
                population.remove(B)
        return population

    def any(self, population=None, n=3):
        """Picks 3 candidates from the population"""
        population = self.population if population is None else population
        smp = random.sample(population, n)
        return smp

    def get_min_max_of_objectives(self, population=None):
        # Find the max and min of objectives in population
        population = self.population if population is None else population
        obj1 = [candidate.objectives.cost for candidate in population]
        obj2 = [candidate.objectives.satisfaction for candidate in population]
        cost_max = max(obj1)
        cost_min = min(obj1)
        sat_max = max(obj2)
        sat_min = min(obj2)
        # print("cost_max, cost_min, sat_max, sat_min")
        # print(cost_max, cost_min, sat_max, sat_min)
        return (cost_max, cost_min), (sat_max, sat_min)


class GeneticAlgorithm(AlgorithmBase):
    def __init__(self, model=NRP, population_size=300, mutation_rate=0.01):
        super(GeneticAlgorithm, self).__init__(model, population_size)
        self.mutation_rate = mutation_rate

    def crossover(self, mom, dad):
        """Single point crossover of mom and dad
        Note: it might generate an invalid child"""
        decision_length = self.model.n_requirements
        assert isinstance(mom, State)
        assert isinstance(dad, State)
        assert decision_length == len(mom.decisions) == len(dad.decisions)
        # Single point crossover generated candidates that were mostly invalid.
        #child = State((mom.decisions[0:decision_length/2] + dad.decisions[decision_length/2:]))
        # Random crossover also genereted similar results.
        child_decs = []
        for i, _ in enumerate(mom.decisions):
            child_decs.append(mom.decisions[i] if random.randint(0,1) else dad.decisions[i])
        assert len(child_decs) == decision_length
        return State(child_decs)

    def mutate(self, person):
        """Mutates the candidate.
        Note: might return an invalid child"""
        mutant_decs = list(person.decisions[:])  # Deep copy
        for i, dec in enumerate(self.model.decisions):
            if random.random() < self.mutation_rate:
                mutant_decs[i] = dec.generate()
        return State(tuple(mutant_decs))

    def fitness(self, person, population, comparator):
        # Compare person with each candidate in population and return the number
        # of candidates it dominated
        return sum([comparator(candidate, person, self.limits) for candidate in population])

    def elitism(self, population, comparator):
        population_list = list(population)
        population_list.sort(key=lambda x:self.fitness(x, population, comparator), reverse=True)
        # Never let the population grow
        keep_size = min(self.population_size, len(population))
        return set(population_list[:keep_size])

    def run_ga(self, comparator=_is_continous_dominated, iterations=2000):
        gen = 0
        global ga_pareto_candidates
        population = deepcopy(self.population)
        self.limits = self.get_min_max_of_objectives(population)
        while gen < iterations:
            children = set()
            for _ in xrange(self.population_size):
                mom, dad = self.any(population, 2)
                child = self.mutate(self.crossover(mom, dad))
                objectives = self.model.evaluate(child)
                if objectives is None:
                    print(".", end="")
                    continue
                else:
                    children.add(child)
            print ("X")
            population.union(children)
            population = self.elitism(population, comparator)
            ga_pareto_candidates = ga_pareto_candidates.union(self.pareto_frontier_candidates(population))
            gen += 1
        return population


class DifferentialEvolution(AlgorithmBase):

    def __init__(self, model=NRP, population_size=50, f=0.25):
        assert population_size > 0
        assert 0.0 < f < 1.0
        self.f = f
        super(DifferentialEvolution, self).__init__(model, population_size)

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
        global de_pareto_candidates
        population = deepcopy(self.population)
        self.limits = self.get_min_max_of_objectives()
        step_ = iterations/ self.population_size
        for i in xrange(iterations):
            if len(population) < 3:
                break
            A, B, C = self.any(population, n=3)
            F = [0 if self.f > random.random() else -1 for _ in range(len(A.decisions))]
            # DE/rand/1.  For binary operators. T = (A OR (F AND( B XOR C )))
            T = _union(A.decisions, _intersection(F, _xor(B.decisions, C.decisions)))
            T = State(T)
            objectives = self.model.evaluate(T)
            if objectives is None:
                print ("The mutant was not acceptable")
                continue
            if comparator(C, T, self.limits):  # If C is dominated by T
                population.remove(C)
                if T in population:
                    pass
                    #print("Duplicate mutant candidate generated")
                else:
                    population.add(T)
            if i % step_ == 0:
                de_pareto_candidates = de_pareto_candidates.union(self.pareto_frontier_candidates(population))

        return population


def plot_graph(population, optimized, pareto):
    #
    x = list()
    y = list()
    for candidate in population:
        x.append(abs(candidate.objectives[0]))
        y.append(candidate.objectives[1])
    plt.plot(x, y, '.g')

    a = list()
    b = list()
    for candidate in optimized:
        a.append(abs(candidate.objectives[0]))
        b.append(candidate.objectives[1])
    plt.plot(a,b, 'ob')

    c = list()
    d = list()
    for candidate in pareto:
        c.append(abs(candidate.objectives[0]))
        d.append(candidate.objectives[1])
    plt.plot(c, d, 'or')

    plt.xlabel('cost ->')
    plt.ylabel('satisfaction ->')
    # limits is ((cost_max, cost_min), (sat_max, sat_min))
    plt.axis([0, 1000, new_limits[1][1], new_limits[1][0]])
    plt.show()

if __name__ == '__main__':
    print("Running GA")
    with open('ga_result.txt', 'w') as ga_res:
        for i in range(20):
            t0 = time.time()
            ga_pareto_candidates = set()
            ga = GeneticAlgorithm(population_size=300)
            ga.generate_population()
            #print (ga.population_size)
            #in_pareto = ga.pareto_frontier_candidates()
            ga_optimized = ga.run_ga(iterations=10)
            ga_pareto = ga.pareto_frontier_candidates(ga_optimized)
            t1 = time.time()
            limits = ga.get_min_max_of_objectives(ga_optimized)
            spread_ = spread(ga_optimized, ga_pareto_candidates)
            igd_ = igd(ga_optimized, ga_pareto_candidates)
            print("spread", spread_, "igd", igd_, "time", t1 - t0)
            ga_res.write(str(spread_) + " " + str(igd_) + " " + str(t1-t0) + "\n")

    # pdb.set_trace()
    # plot_graph(ga.population, in_pareto, limits)
    # plot_graph(ga_optimized, ga_pareto, limits)
    print ("Running DE")
    with open('de_result.txt', 'w') as de_res:
        for i in range(20):
            t0 = time.time()
            de = DifferentialEvolution(population_size=300)
            de.generate_population()
            #pareto = de.pareto_frontier_candidates()
            optimized = de.run_de(comparator=_is_continous_dominated)
            de_pareto = de.pareto_frontier_candidates(optimized)
            t1 = time.time()
            limits1 = de.get_min_max_of_objectives(optimized)
            #opti = de.prune_population(optimized)
            spread_ = spread(optimized, de_pareto_candidates)
            igd_ = igd(optimized, de_pareto_candidates)
            print("spread", spread_, "igd", igd_, "time", t1 - t0)
            de_res.write(str(spread_) + " " + str(igd_) + " " + str(t1 - t0) + "\n")
    # (cost_max, cost_min), (sat_max, sat_min)
    new_limits = ((max(limits[0][0], limits1[0][0]), min(limits[0][1], limits1[0][1])),
                  (max(limits[1][0], limits1[1][0]), min(limits[1][1], limits1[1][1])))
    plot_graph(de.population, optimized, de_pareto)
    plot_graph(ga.population, ga_optimized, ga_pareto)
    # plot_graph(de.population, pareto, limits)
    #plot_graph(optimized, op_pareto, limits)
    #pdb.set_trace()
    #de_pareto_candidates = de.prune_population(de_pareto_candidates)
    # ga_pareto_candidates = ga.prune_population(ga_pareto_candidates)
    #plot_graph(de_pareto_candidates, ga_pareto_candidates, limits)
