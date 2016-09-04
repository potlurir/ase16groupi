# Employee class example.

class Employee(object):
    """ Employee class to pretty print and sort by age """

    def __init__(self, name, age):
        super(Employee, self).__init__()
        self.name = name
        self.age = age

    def __repr__(self):
        return "Name: %s, Age: %s" % (self.name, self.age)

    def __lt__(self, other):
        return self.age < other.age


e1 = Employee("e1", 24)
e2 = Employee("e2", 30)
e3 = Employee("e3", 26)
e4 = Employee("e4", 25)
e5 = Employee("e5", 26)
e6 = Employee("e6", 26)

print "++++++++++++ PART 1 ++++++++++++"
print e1.__repr__()
print e2.__repr__()
print e3.__repr__()
print e4.__repr__()
print e5.__repr__()
print e6.__repr__()
print "++++++++++++++++++++++++++++++++"

print "++++++++++++ PART 2 ++++++++++++"
print "Sorted List of Employees"

listOfEmployees = [e1, e2, e3, e4, e5, e6]
listOfEmployees.sort()
for e in listOfEmployees:
    print e
print "++++++++++++++++++++++++++++++++"
