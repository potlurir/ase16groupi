from __future__ import division

from random import randint
import sys
sys.dont_write_bytecode = True


class NextReleaseProblem(object):
    def __init__(self, requirements, customers, budget, max_importance, max_satisfaction):
        self.requirements = requirements
        self.customers = customers
        self.budget = budget
        self.cost = [randint(1, self.budget) for _ in xrange(self.requirements)]
        self.customer_importance = [randint(1, max_importance) for _ in xrange(self.customers)]
        self.customer_satisfaction = [[randint(1, max_satisfaction) for _ in xrange(self.requirements)]
                                      for _ in xrange(self.customers)]
        self.satisfaction = [0 for _ in xrange(self.requirements)]
        for i in xrange(self.requirements):
            for j in xrange(self.customers):
                self.satisfaction[i] += self.customer_importance[j] * self.customer_satisfaction[j][i]
        self.satR = sum(self.satisfaction)
        self.MI = 1.0

    def __str__(self):
        return "Requirements: {0}, Customers: {1}, Budget: {2}, Satisfaction: {3}, satR: {4}".\
            format(self.requirements, self.customers, self.budget, self.satisfaction, self.satR)

    # I highly doubt this.
    def get_nij(self, j):
        return self.MI * (self.satisfaction[j] / self.cost[j])

    def get_nodes(self):
        return self.requirements

    def get_t0(self):
        return 1/self.satR

    def initialize_the_mandatory_neighbourhood(self, ant):
        for i in xrange(self.get_nodes()):
            if (i != ant.current_node) and (self.cost[i] <= self.budget):
                ant.nodes_to_visit.append(i)

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

    @staticmethod
    def better(ant, best_ant):
        return best_ant is None or ant.tour_length > best_ant.tour_length

    def get_delta_tau(self, ant):
        return ant.tour_length/self.satR


if __name__ == '__main__':
    nrp = NextReleaseProblem(20, 5, 25)
    print str(nrp)
