from __future__ import print_function
from __future__ import division

from random import randint
import random
import tabulate
#random.seed(1)
"""
This model of Next Release Problem is based on the paper
A Study of the Multi-Objective Next Release Problem by
J. J. Durillo et. al. in the
1st International Symposium on Search Based Software Engineering
"""


class Decision(object):
    def __init__(self, name, low, high, generator_fn=randint):
        assert low < high, "low > high for Decision {0}".format(name)
        self.name = name
        self.low = low
        self.high = high
        self.generator_fn = generator_fn

    def generate(self):
        return self.generator_fn(self.low, self.high)

    def __repr__(self):
        return "{0} low= {1} high= {2}".format(self.name, self.low, self.high)


class Objective(object):
    def __init__(self, name, do_minimize=True):
        self.name = name
        self.do_minimize = do_minimize

    def __repr__(self):
        return "{0}".format(self.name)


class Requirement(object):
    cost_min = 1
    cost_max = 200

    def __init__(self, name):
        # Cost is the economical cost for satisfying a requirement
        self.name = name
        self.cost = randint(Requirement.cost_min, Requirement.cost_max)

    def __repr__(self):
        return "{0} Cost= {1}".format(self.name,str(self.cost))


class Client(object):
    imp_min = 1
    imp_max = 5

    def __init__(self, name):
        # Each client has associated a value which reflects its degree of importance
        # as a customer for the software company
        self.name = name
        self.value = randint(Client.imp_min, Client.imp_max)

    def __repr__(self):
        return "{0} value= {1}".format(self.name, self.value)


class NRP(object):
    def __init__(self, n_requirements=10, n_releases=1, n_clients=10, density=0, budget=100):

        self.n_requirements = n_requirements
        self.n_releases = n_releases
        self.n_clients = n_clients
        self.density = density  # Currently considering only independent requirements
        self.budget = budget
        # to include a requirement or not in a release is a decision
        # If a requirement is never to me satisfied then its value will be -1
        # otherwise its value would be the release number during which it will be developed
        # For single release projects it can be either -1 (don't develop it) or 0 (ship it in current release)
        self.decisions = [Decision('d'+str(i), low=-1, high=n_releases-1) for i in range(n_requirements)]
        # Currently two objectives
        # 1) Total cost in developing the requirements
        # 2) Satisfaction of all the customers
        self.objectives = [Objective('cost', do_minimize=True), Objective('satisfaction', do_minimize=False)]

        self.clients = None
        self.requirements = None
        self.precedence = None
        self.importance_matrix = None

        self.generate_random_data()

    def __str__(self):
        ss = "\nRequirements : {0}\n".format(self.requirements)
        ss += "\nClients : {0}\n".format(self.clients)
        ss += "\nImportance Matrix\n"
        # for aasd in self.importance_matrix:
        #     ss += "\n" + str(aasd)
        ss += tabulate.tabulate(self.importance_matrix)
        ss += "\nDecisions: {0}\n".format(self.decisions)
        ss += "\nObjectives: {0}\n".format(self.objectives)
        return ss

    def generate_random_data(self):
        """ Creates imaginary random clients, requirements and clients
         value for a requirement
        """
        def generate_importance():
            # TODO: Find a way to not hard-code these min and max values
            importance_min = 0
            importance_max = 100
            return [[randint(importance_min, importance_max) for _ in range(self.n_requirements)] for _ in range(self.n_clients)]

        self.clients = [Client('c' + str(i)) for i in range(self.n_clients)]
        self.requirements = [Requirement('r'+str(i)) for i in range(self.n_requirements)]
        # importance_matrix[i][j] represents the importance of requirement r_j for customer c_i
        self.importance_matrix = generate_importance()

    def calculate_cost(self, decs):
        """ Returns the cost of implementing the requirements in decs"""
        return sum([self.requirements[i].cost for i, dec in enumerate(decs) if dec != -1])

    def is_budget_ok(self, decs):
        # Checks if the requirements selected don't exceed the budget
        # TODO: For multi-release projects, this will need modification
        return self.calculate_cost(decs) <= self.budget

    def is_dependency_ok(self, decs):
        # Checks if the dependencies among the requirements is satisfied
        # TODO: For dependent requirements, this needs to be implemented
        return True

    def any(self):
        """ Generates a set of requirements R' """
        for _ in range(100):
            decs = [dec.generate() for dec in self.decisions]
            if self.is_budget_ok(decs) and self.is_dependency_ok(decs):
                return decs
        raise Exception("Could not generate a valid decision in 100 attempts")

    def any3(self):
        """ Generates three different set of requirements R', R'' and R''' """
        first = self.any()
        second = first
        while first == second:
            second = self.any()
        third = first
        while third == first or third == second:
            third = self.any()
        return first, second, third

    def evaluate(self, decisions):
        pass


if __name__ == '__main__':
    nrp = NRP(n_requirements=20, budget=1000)
    print(nrp)
    one = nrp.any()

    two, three, four = nrp.any3()
    print (one, nrp.calculate_cost(one))
    print(two, nrp.calculate_cost(two))
    print(three, nrp.calculate_cost(three))
    print(four, nrp.calculate_cost(four))
