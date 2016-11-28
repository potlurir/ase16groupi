from NextReleaseProblem import NextReleaseProblem
from random import randint, uniform
from threading import Thread
import math


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

    def reset(self):
        self.current_node = -1
        self.tour_length = 0
        self.nodes_to_visit = []
        self.tour = []
        self.path = [[-1 for _ in xrange(self.aco.problem.n_requirements)]
                     for _ in xrange(self.aco.problem.n_requirements)]

    def init(self):
        self.reset()
        self.current_node = randint(0, self.aco.problem.n_requirements - 1)
        self.tour.append(self.current_node)

    def run(self):
        self.init()

    def explore(self):
        pass

    def clone(self):
        pass


class Ant4ACS(Ant):
    def __init__(self, aco):
        super(Ant4ACS, self).__init__(aco)
        # Probability of best choice in tour construction
        self.Q0 = 0.9
        # Decrease local pheromone
        self.P = 0.1

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
            self.aco.problem.update_the_mandatory_neighbourhood(self.tour, self.nodes_to_visit)
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
        max_val = float("INF")
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
        self.nodes_to_visit.remove(next_node)
        if next_node == -1:
            raise Exception("Next node is -1")
        return next_node

    def local_update_rule(self, j):
        evaporation = (1.0 - self.P) * self.aco.getTau(self.current_node, j)
        deposition = self.P * self.aco.p.getT0()
        self.aco.set_tau(self.current_node, j, evaporation + deposition)
        self.aco.set_tau(j, self.current_node, evaporation + deposition)


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


class NRPTest(object):
    def __init__(self):
        self.num_of_ants = 10
        self.iterations = 10
        self.p = NextReleaseProblem(20, 5, 25)
        acs = AntColonySystem(self.num_of_ants, self.iterations, self.p)
        acs.ants = [Ant4ACS(acs) for _ in xrange(acs.num_of_ants)]
        best_ant = acs.solve()
        print best_ant.tour


if __name__ == '__main__':
    NRPTest()
