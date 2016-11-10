from __future__ import division

from random import random, randint
import sys, os, inspect
from jmoo_objective import *
from jmoo_decision import *
from jmoo_problem import jmoo_problem
from Requirement import Requirement
from Client import Client
from Release import Release
from printtable import PrintTable


class MONRP(jmoo_problem):

    def __init__(self, requirements, releases, clients, density, budget):
        # |x_i + y_i|
        names = ["x"+str(i+1) for i in range(requirements)]
        lows =  [-1 for _ in xrange(requirements)]
        ups =   [(releases - 1) for _ in xrange(requirements)]
        self.decisions = [jmoo_decision(names[i], lows[i], ups[i]) for i in range(requirements)]
        self.objectives = [jmoo_objective("f1", False), jmoo_objective("f2", True), jmoo_objective("f3", False)]
        self.trequirements = requirements
        self.treleases = releases
        self.tclients = clients
        self.tdensity = density
        self.tbudget = budget
        self.requirement = None
        self.client = None
        self.release = None
        self.precedence = []
        self.generate_data()

    def generate_precedence(self):
        precedence = [[0 for _ in xrange(self.trequirements)]
                      for _ in xrange(self.trequirements)]
        temp = []
        for _ in xrange(int(self.tdensity * self.trequirements * 0.01)):
            while True:
                row = randint(0, self.trequirements - 1)
                col = randint(0, self.trequirements - 1)
                t = row * 1000 + col
                if t not in temp:
                    temp.append(t)
                    break
        # print "Done"
        for t in temp:
            precedence[int(t/1000)][int(t%1000)] = 1
        return precedence

    def generate_data(self):
        self.requirement = [Requirement(i) for i in xrange(self.trequirements)]
        self.client = [Client(i, self.trequirements) for i in xrange(self.tclients)]
        budget_release = int((sum(req.cost for req in self.requirement) *
                             (self.tbudget/100))/self.treleases)
        self.release = [Release(i, budget_release) for i in xrange(self.treleases)]
        self.precedence = self.generate_precedence()

    def print_data(self):
        table = PrintTable(client_data=self.client,
                           precedence_data=self.precedence,
                           requirement_data=self.requirement,
                           release_data=self.release)
        print table.clients()
        print table.requirements()
        print table.precedence()
        print table.releases()

    def constraint1(self, x_i, y_i):
        cost = [0 for _ in xrange(self.treleases)]
        for i, y in enumerate(y_i):
            if y != 0:
                assert(self.requirement[y].id == y), "Indexing Error!"
                assert(x_i[i] <= self.treleases)
                cost[x_i[i]] += self.requirement[i].cost
        # print cost, [b.budget for b in self.release], sum(cost), sum([b.budget for b in self.release])
        extra = 0
        for c, b in zip(cost, self.release):
            if c > b.budget:
                extra -= (c - b.budget)
        return extra

    def constraint2(self, x_i, y_i):
        for y in y_i:
            if y != 0:
                relation = self.precedence[y]
                if sum(relation) == 0:  # no dependencies
                    return True
                else:
                    current_release = x_i[y] # when was y implement
                    for count, p in enumerate(relation):
                        if p != 0:
                            # the dependency 'count' wasn't implemented before current release
                            if x_i[count] > current_release:
                                return False
                    return True

    def printHeader(self):
        print "Multi-Objective NRP:",
        print "Requirements: " + str(self.trequirements) + ",",
        print "Releases: " + str(self.treleases) + ",",
        print "Clients: " + str(self.tclients) + ",",
        print "Density: " + str(self.tdensity) + ",",
        print "Budget: " + str(self.tbudget)
        # print "Decisions: " + str([(d.name, d.low, d.up) for d in self.decisions])

    def evaluate(self, input = None):

        if input:
            input = input[:self.trequirements]
            x_i = [int(round(float(no), 0)) for no in input]  # when is r_i is implemented
            y_i = [1 if x != -1 else 0 for x in x_i]  # whether r_i would be implemented
            assert(len(x_i) == len(y_i)), "Both the list should be of the same size"
            temp = self.constraint1(x_i, y_i)  # This is dirty need to know a better trick
            if temp != 0:
                output = [temp, 1e32, 0]
                for i, objective in enumerate(self.objectives):
                    objective.value = output[i]
                return output
            elif self.constraint2(x_i, y_i) is False:
                output = [0, 1e32, 0]
                for i, objective in enumerate(self.objectives):
                    objective.value = output[i]
                return output
            else:
                return_score = 0
                cost = 0
                for i in xrange(self.trequirements):
                    score = sum([j.importance[i] * j.weight for j in self.client])
                    x = x_i[i]
                    return_score += (score * (self.treleases - x + 1) - self.requirement[i].risk) * y_i[i]
                    # reduce the cost (from A Study of the Multi-Objective Next Release Problem)
                    cost += self.requirement[i].cost

                # Maximize the satisfaction (from A Study of the Multi-Objective Next Release Problem)
                satisfaction = 0
                for c in xrange(self.tclients):
                    for i in xrange(self.trequirements):
                        if y_i != 0:
                            satisfaction += self.client[c].importance[i]

                output = [return_score, cost, satisfaction]
                for i, objective in enumerate(self.objectives):
                    objective.value = output[i]
                return output

        else:
            assert(False), "BOOM"
            exit()

    def evalConstraints(prob,input = None):
        return False


if __name__ == "__main__":
    problem = MONRP(50, 5, 5, 100, 80)
    problem.printHeader()
    problem.print_data()
    # print problem.evaluate(problem.requirement)







