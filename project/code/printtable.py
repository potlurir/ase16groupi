from prettytable import PrettyTable

class PrintTable(object):

    def __init__(self, client_data=None, precedence_data=None,
                 requirement_data=None, release_data=None):
        self.client_data = client_data
        self.precedence_data = precedence_data
        self.requirement_data = requirement_data
        self.release_data = release_data

    def clients(self):
        t = PrettyTable(['Client', 'Weight', 'Importance'])
        for index, c in enumerate(self.client_data):
            t.add_row([index, c.weight, "".join(str(e) for e in c.importance)])
        return t

    def requirements(self):
        # 'Client', 'Weight', 'Importance',
        t = PrettyTable(['Requirement-Id', 'Requirement-Cost',
                         'Requirement-Risk'])
        # for index, c in enumerate(self.client_data):
        for i, r in enumerate(self.requirement_data):
            r_id = i
            cost = r.cost
            risk = r.risk
            t.add_row([r_id+1, cost, risk])
        return t

    def releases(self):
        t = PrettyTable(['Release-Id', 'Budget'])
        for i, r in enumerate(self.release_data):
            t.add_row([i+1, r.budget])
        return t

    def precedence(self):
        t = PrettyTable(['Precedence-Id', 'Value'])
        for i, r in enumerate(self.precedence_data):
            t.add_row([i+1, "".join(str(e) for e in r)])
        return t