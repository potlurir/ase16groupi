from __future__ import division

from random import randint, uniform
import math


class Ant(object):
    ANT_ID = 1

    def __init__(self, aco):
        # Importance of trail
        self.ALPHA = 1
        # Importance of heuristic evaluate
        self.BETA = 2
        self.id = Ant.ANT_ID
        Ant.ANT_ID += 1
        self.aco = aco
        self.tour = []
        self.current_node = None
        self.path = [[]]
        self.nodes_to_visit = []
        self.tour_length = 0
        self.reset()

    def reset(self):
        self.current_node = -1
        self.tour_length = 0
        self.nodes_to_visit = []
        self.tour = []
        self.path = [[-1 for _ in xrange(self.aco.problem.get_nodes())]
                     for _ in xrange(self.aco.problem.get_nodes())]

    def run(self):
        self.init()
        self.explore()
        # Notify Observer here
        # Work in Progress

    def init(self):
        self.reset()
        self.current_node = randint(0, self.aco.problem.get_nodes() - 1)
        self.tour.append(self.current_node)
        self.aco.problem.initialize_the_mandatory_neighbourhood(self)

    # Abstract method
    def explore(self):
        pass

    # Abstract method
    def clone(self):
        pass


class Ant4ACS(Ant):
    def __init__(self, aco):
        super(Ant4ACS, self).__init__(aco)
        # Probability of best choice in tour construction
        self.Q0 = 0.9
        # Decrease local pheromone
        self.P = 0.1

    def __str__(self):
        return "Ant Id: {0}, ALPHA: {1}, BETA: {2}, currentNode: {3}".\
            format(self.id, self.ALPHA, self.BETA, self.current_node)

    def explore(self):
        while self.nodes_to_visit:
            if uniform(0, 1) <= self.Q0:
                next_node = self.do_exploitation()
            else:
                next_node = self.do_exploration()
            self.local_update_rule(next_node)
            self.tour.append(next_node)
            self.path[self.current_node][next_node] = 1
            self.path[next_node][self.current_node] = 1
            self.aco.problem.update_the_mandatory_neighbourhood(self)
            self.current_node = next_node

    def do_exploration(self):
        temp_sum = 0.0
        for j in self.nodes_to_visit:
            if self.aco.get_tau(self.current_node, j) == 0.0:
                raise Exception("Tau is 0.0")
            tij = math.pow(self.aco.get_tau(self.current_node, j), self.ALPHA)
            nij = math.pow(self.aco.problem.get_nij(self.current_node, j), self.BETA)
            temp_sum += tij + nij
        if temp_sum == 0.0:
            raise Exception("Sum is 0.0")
        probability = [0 for _ in xrange(self.aco.p.get_nodes())]
        sum_of_probability = 0.0
        for j in self.nodes_to_visit:
            tij = math.pow(self.aco.get_tau(self.current_node, j), self.ALPHA)
            nij = math.pow(self.aco.problem.get_nij(self.current_node, j), self.BETA)
            probability[j] = (tij * nij) / temp_sum
            sum_of_probability += probability[j]
        next_node = RouletteWheel.select(probability, sum_of_probability)
        self.nodes_to_visit.remove(next_node)
        return next_node

    def do_exploitation(self):
        max_val = float("-INF")
        next_node = -1
        for j in self.nodes_to_visit:
            if self.aco.get_tau(self.current_node, j) == 0.0:
                raise Exception("Tau is 0.0")
            tij = self.aco.get_tau(self.current_node, j)
            nij = math.pow(self.aco.problem.get_nij(self.current_node, j), self.BETA)
            value = tij * nij
            if value > max_val:
                max_val = value
                next_node = j
        if next_node == -1:
            raise Exception("Next node is -1")
        self.nodes_to_visit.remove(next_node)
        return next_node

    def local_update_rule(self, j):
        evaporation = (1.0 - self.P) * self.aco.get_tau(self.current_node, j)
        deposition = self.P * self.aco.p.get_t0()
        self.aco.set_tau(self.current_node, j, evaporation + deposition)
        self.aco.set_tau(j, self.current_node, evaporation + deposition)

    def clone(self):
        ant = Ant4ACS(self.aco)
        ant.id = self.id
        ant.current_node = self.current_node
        ant.tour_length = self.tour_length
        ant.tour = self.tour
        ant.path = list(self.path)
        return ant


class RouletteWheel(object):
    @staticmethod
    def select(probability, sum_of_probability):
        j = 0
        p = probability[j]
        r = uniform(0.0, sum_of_probability)
        while p < r:
            j += 1
            p += probability[j]
        return j
