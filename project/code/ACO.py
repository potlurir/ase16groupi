from __future__ import division

from NextReleaseProblem import NextReleaseProblem
from Ant import Ant4ACS

import sys
sys.dont_write_bytecode = True
import traceback


class ACO(object):
    def __init__(self, num_of_ants, iterations, problem):
        self.RHO = 0.1
        self.ants = []
        self.num_of_ants = num_of_ants
        self.tau = None
        self.problem = problem
        self.iterations = iterations
        self.it = 0
        self.finished_ants = 0
        self.best_ant = None

    def solve(self):
        self.initialize_data()
        while not self.termination_condition():
            try:
                self.construct_ants_solution()
                self.update_pheromones()
            except Exception as e:
                print e
                break
        return self.best_ant

    def initialize_data(self):
        self.initialize_pheromones()
        self.initialize_ants()

    def initialize_pheromones(self):
        self.tau = [[self.problem.get_t0() for _ in xrange(self.problem.get_nodes())]
                    for _ in xrange(self.problem.get_nodes())]
        # print self.tau
        # sys.exit()

    def termination_condition(self):
        self.it += 1
        return self.it > self.iterations

    def update_pheromones(self):
        self.global_update_rule()

    def construct_ants_solution(self):
        for ant in self.ants:
            try:
                ant.run()
            except Exception as e:
                print e
                traceback.print_exc()

    # I have to fix this. Restart thread at last line.
    def update(self, ant):
        ant.tourLength = self.problem.evaluate(ant)
        if self.problem.better(ant, self.best_ant):
            print "I am cloning"
            self.best_ant = ant.clone()
        self.finished_ants += 1
        if self.finished_ants == self.num_of_ants:
            self.finished_ants = 0
            # Restart Thread

    def get_tau(self, i=None, j=None):
        # print "Hey I am Tau: {0}, {1}".format(i, j)
        return self.tau if (i is None or j is None) else self.tau[i][j]

    def set_tau(self, i, j, value):
        self.tau[i][j] = value

    def global_update_rule(self):
        pass

    def initialize_ants(self):
        pass


class AntColonySystem(ACO):
    def __init__(self, ants, iterations, problem):
        super(AntColonySystem, self).__init__(ants, iterations, problem)

    def initialize_ants(self):
        self.ants = [Ant4ACS(self) for _ in xrange(self.num_of_ants)]
        for ant in self.ants:
            ant.register_observer(self)

    def global_update_rule(self):
        for i in xrange(self.problem.get_nodes()):
            for j in xrange(i, self.problem.get_nodes()):
                if i != j and self.best_ant.path[i][j] == 1:
                    delta_tau = self.problem.get_delta_tau(self.best_ant)
                    evaporation = (1.0 - self.RHO) * self.tau[i][j]
                    deposition = self.RHO * delta_tau
                    self.tau[i][j] = evaporation + deposition
                    self.tau[j][i] = evaporation + deposition


class NRPTest(object):
    def __init__(self):
        self.num_of_ants = 1
        self.iterations = 1
        self.p = NextReleaseProblem(20, 5, 25)
        aco = AntColonySystem(self.num_of_ants, self.iterations, self.p)
        # for ant in aco.ants:
        #     print str(ant)
        best_ant = aco.solve()
        print best_ant.tour


if __name__ == '__main__':
    NRPTest()
