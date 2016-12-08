from __future__ import division

from NextReleaseProblem import NextReleaseProblem
from Ant import Ant4ACS
from matplotlib import pyplot as plt
import traceback
import sys

sys.dont_write_bytecode = True


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
        self.best_sols = []

    def solve(self):
        self.initialize_data()
        while not self.termination_condition():
            self.construct_ants_solution()
            self.update_pheromones()
            self.best_sols.append(self.best_ant)

    def initialize_data(self):
        self.initialize_pheromones()
        self.initialize_ants()

    def initialize_pheromones(self):
        self.tau = [[self.problem.get_t0() for _ in xrange(self.problem.get_nodes())]
                    for _ in xrange(self.problem.get_nodes())]

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

    def update(self, ant):
        ant.tour_length = self.problem.evaluate(ant)
        if self.problem.better(ant, self.best_ant):
            self.best_ant = ant.clone()
        self.finished_ants += 1
        if self.finished_ants == self.num_of_ants:
            self.finished_ants = 0

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
    def __init__(self, num_of_ants, iterations, problem):
        super(AntColonySystem, self).__init__(num_of_ants, iterations, problem)

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
        # Number of ants represents number of releases.
        self.num_of_ants = 1
        # Number of iterations
        self.iterations = 10
        # NextReleaseProblem(requirements, customers, budget, density, max_cost, max_importance, max_satisfaction)
        self.p = NextReleaseProblem(200, 10, 1000, 20, 100, 10, 10)
        aco = AntColonySystem(self.num_of_ants, self.iterations, self.p)
        aco.solve()
        solution = []
        # print str(self.p)
        # print aco.best_sols.tour
        sols2 = []
        for best_ant in aco.best_sols:
            best_ant.tour.sort()
            cost = sum(self.p.cost[i] for i in best_ant.tour)
            solution.append((cost, best_ant.tour_length))
            sols2.append(" ".join(str(node) for node in best_ant.tour))
        # print list(set(sols2))
        # print list(set(solution))
        solution = list(set(solution))
        plt.title('Cost and Satisfaction graph for Next Release Problem')
        x_coordinates = [coordinate[0] for coordinate in solution]
        y_coordinates = [coordinate[1] for coordinate in solution]
        print x_coordinates, y_coordinates
        plt.scatter(*zip(*solution))
        plt.xlabel('cost ->')
        plt.ylabel('satisfaction ->')
        plt.show()


if __name__ == '__main__':
    NRPTest()
