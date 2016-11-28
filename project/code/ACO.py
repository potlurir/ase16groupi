from NextReleaseProblem import NextReleaseProblem
from Ant import Ant4ACS
from threading import Thread

import sys
sys.dont_write_bytecode = True


class AntThread(Thread):
    def __init__(self, func, name):
        super(AntThread, self).__init__()
        self.func = func
        self.name = name

    def run(self):
        print "Thread name: " + self.name
        self.func()


class ACO(object):
    def __init__(self, num_of_ants, iterations, problem):
        self.RHO = 0.1
        self.ants = []
        self.num_of_ants = num_of_ants
        self.tau = None
        self.iterations = iterations
        self.problem = problem
        self.it = 0
        self.finished_ants = 0
        self.best_ant = None

    def solve(self):
        self.initialize_data()
        while not self.termination_condition():
            self.construct_ants_solution()
            self.update_pheromones()
        return self.best_ant

    def initialize_data(self):
        self.initialize_pheromones()

    def initialize_pheromones(self):
        self.tau = [[self.problem.get_t0() for _ in xrange(self.problem.get_nodes())]
                    for _ in xrange(self.problem.get_nodes())]

    def termination_condition(self):
        self.it += 1
        return self.it > self.iterations

    def update_pheromones(self):
        self.global_update_rule()

    def construct_ants_solution(self):
        for i in xrange(self.num_of_ants):
            try:
                t = AntThread(self.ants[i], "Ant: " + str(self.ants[i].id))
                t.start()
            except Exception as e:
                print e

    def get_tau(self, i=None, j=None):
        return self.tau if not (i and j) else self.tau[i][j]

    def set_tau(self, i, j, value):
        self.tau[i][j] = value

    def global_update_rule(self):
        pass


class AntColonySystem(ACO):
    def __init__(self, ants, iterations, problem):
        super(AntColonySystem, self).__init__(ants, iterations, problem)

    def global_update_rule(self):
        for i in xrange(self.problem.get_nodes()):
            for j in xrange(i, self.problem.get_nodes()):
                if i != j and self.best_ant.path[i][j] == 1:
                    delta_tau = self.problem.get_delta_tau()
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
        aco.ants = [Ant4ACS(aco) for _ in xrange(aco.num_of_ants)]
        for ant in aco.ants:
            print str(ant)
        # best_ant = acs.solve()
        # print best_ant.tour


if __name__ == '__main__':
    NRPTest()
