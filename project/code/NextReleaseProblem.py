from __future__ import division

from random import randint
from math import exp
import sys
sys.dont_write_bytecode = True


class NextReleaseProblem(object):
    def __init__(self, requirements, customers, budget, density, max_cost, max_importance, max_satisfaction):
        self.requirements = requirements
        self.customers = customers
        self.budget = budget
        self.density = density
        self.cost = [randint(1, max_cost) for _ in xrange(self.requirements)]
        self.customer_importance = [randint(1, max_importance) for _ in xrange(self.customers)]
        self.customer_satisfaction = [[randint(1, max_satisfaction) for _ in xrange(self.requirements)]
                                      for _ in xrange(self.customers)]
        self.satisfaction = [0 for _ in xrange(self.requirements)]
        for i in xrange(self.requirements):
            for j in xrange(self.customers):
                self.satisfaction[i] += self.customer_importance[j] * self.customer_satisfaction[j][i]
        self.satR = sum(self.satisfaction)
        self.MI = 1.0
        self.precedence_matrix = self.generate_precedence()
        cost_min = min(self.cost)
        cost_max = max(self.cost)
        satisfaction_min = min(self.satisfaction)
        satisfaction_max = max(self.satisfaction)
        self.limits = [[cost_min, cost_max], [satisfaction_min, satisfaction_max]]

    def generate_precedence(self):
        precedence = [[0 for _ in xrange(self.requirements)] for _ in xrange(self.requirements)]
        temp = []
        for _ in xrange(int(self.density * self.requirements * 0.01)):
            while True:
                row = randint(0, self.density - 1)
                col = randint(0, self.density - 1)
                t = row * 1000 + col
                if t not in temp:
                    temp.append(t)
                    break
        # print "Done"
        for t in temp:
            precedence[int(t / 1000)][int(t % 1000)] = 1
        return precedence

    def __str__(self):
        return "Requirements: {0}, Customers: {1}, Budget: {2}, Satisfaction: {3}, satR: {4}".\
            format(self.requirements, self.customers, self.budget, self.satisfaction, self.satR)

    # I highly doubt this.
    def get_wj(self, j):
        return self.MI * (self.satisfaction[j] / self.cost[j])

    def get_nodes(self):
        return self.requirements

    def get_t0(self):
        return 1/self.satR

    def initialize_the_mandatory_neighbourhood(self, ant):
        for i in xrange(self.get_nodes()):
            if (i != ant.current_node) and (self.cost[i] <= self.budget):
                ant.nodes_to_visit.append(i)
        # print "Current Node: {1} , Neighbourhood: {0}".format(ant.nodes_to_visit, ant.current_node)

    def update_the_mandatory_neighbourhood(self, ant):
        nodes_to_remove = []
        total_cost = 0.0
        for i in ant.tour:
            total_cost += self.cost[i]
        # print "Total cost of Tour: {0}".format(total_cost)
        for i in ant.nodes_to_visit:
            if total_cost + self.cost[i] > self.budget:
                nodes_to_remove.append(i)
        for i in nodes_to_remove:
            ant.nodes_to_visit.remove(i)

    def evaluate(self, ant):
        temp_sum = 0.0
        for i in ant.tour:
            temp_sum += self.satisfaction[i]
        return temp_sum

    def better(self, ant, best_ant):

        def normalize(val, _max, _min):
            # Let's see if this ever generates divide by zero exception.
            _max = max(_max, val)
            _min = min(_min, val)
            return (val - _min) / float(_max - _min)

        def exp_loss(c, t, w, n):
            return -1 * exp(w * (c - t) / float(n))

        def loss(c, t):
            c_norm = [normalize(val, limit[0], limit[1]) for val, limit in zip(c, self.limits)]
            t_norm = [normalize(val, limit[0], limit[1]) for val, limit in zip(t, self.limits)]
            n = 2
            losses = [exp_loss(c, t, w, n) for c, t, w in zip(c_norm, t_norm, [1, 1])]
            return sum(losses) / float(n)
        if best_ant is None:
            return True
        cost1 = sum(self.cost[i] for i in ant.tour)
        satisfaction1 = self.evaluate(ant)
        cost2 = sum(self.cost[i] for i in best_ant.tour)
        satisfaction2 = self.evaluate(best_ant)
        c = (cost1, cost2)
        t = (satisfaction1, satisfaction2)
        l1 = loss(c, t)  # l1 is loss associated with picking C over T
        l2 = loss(t, c)  # l2 is loss associated with picking T over C
        return l2 < l1  # Return true if the loss associated with picking T is less

    # @staticmethod
    # def better(ant, best_ant):
    #     return best_ant is None or ant.tour_length > best_ant.tour_length

    def get_delta_tau(self, ant):
        return ant.tour_length/self.satR


if __name__ == '__main__':
    nrp = NextReleaseProblem(100, 10, 1000, 0, 10, 10, 10)
    # print str(nrp)
    print nrp.customer_importance
    print nrp.cost
    for s in nrp.customer_satisfaction:
        print s
    # for p in nrp.precedence_matrix:
    #     print p
