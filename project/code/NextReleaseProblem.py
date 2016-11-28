from __future__ import division

# from random import randint, seed
import sys
sys.dont_write_bytecode = True


class NextReleaseProblem(object):
    def __init__(self, requirements, customers, budget):
        # seed(0)
        self.requirements = requirements
        self.customers = customers
        self.budget = budget
        # self.cost = [randint(0, self.budget) for _ in xrange(self.requirements)]
        self.cost = [1, 4, 2, 3, 4, 7, 10, 2, 1, 3, 2, 5, 8, 2, 1, 4, 10, 4, 8, 4]
        self.customer_importance = [4, 4, 3, 5, 5]
        # self.customer_importance = [randint(0, 5) for _ in xrange(self.customers)]
        # self.customer_satisfaction = [[randint(0, 5) for _ in xrange(self.requirements)]
        #                               for _ in xrange(self.customers)]
        self.customer_satisfaction = [[4, 2, 1, 2, 5, 5, 2, 4, 4, 4, 2, 3, 4, 2, 4, 4, 4, 1, 3, 2],
                                      [4, 4, 2, 2, 4, 5, 1, 4, 4, 5, 2, 3, 2, 4, 4, 2, 3, 2, 3, 1],
                                      [5, 3, 3, 3, 4, 5, 2, 4, 4, 4, 2, 4, 1, 5, 4, 1, 2, 3, 3, 2],
                                      [4, 5, 2, 3, 3, 4, 2, 4, 2, 3, 5, 2, 3, 2, 4, 3, 5, 4, 3, 2],
                                      [5, 4, 2, 4, 5, 4, 2, 4, 5, 2, 4, 5, 3, 4, 4, 1, 1, 2, 4, 1]]
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
    def get_nij(self, i, j):
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
            total_cost = self.cost[i]
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
    # print nrp.cost
    # print nrp.customer_importance
    # print nrp.customer_satisfaction
