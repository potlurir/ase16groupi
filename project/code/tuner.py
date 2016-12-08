from __future__ import division, print_function
"""
This module uses Simulated Annealing to tune the parameters for DE and GA
"""
import math, random
from de import DifferentialEvolution
import pdb


def generate_random_f(): return round(random.random(), 2)

"""
Now the question was for a maximization problem as highlighted in Q-2a.
So if it has to come in this function e_new has to be less than e_old.
Since the function has to return probability the valid return value has to be between 0 and 1.
We compute probability by raising e to an exponent. Since e > 1 (2.73),
the exponent has to be negative to make sure that probability is less than 1.
So the numerator of the exponent has to be (e_new - e_old).

Most have you have taken t=k/k_max . At the start t = k/k_max will be a small value,
so if you use P = e^(e_new - e_old)/t, P will be a small value considering the numerator
is negative and t is close to 0. But ideally you need the probability to be large at the start.
Hence, you will need to subtract the denominator with 1.
Thus, P = e^(e_new - e_old)/(1-t) where t =k/k_max
"""


def probability(old, new, k): return math.exp((new - old) / k)
# I am using it as random.random() < probability(), hence I need probability to be small at start.


def normalize(de):
    """Baseline study to find the max-min of objective,
    so that the value can be normalized."""
    _max = float('-inf')
    _min = -1 * _max
    for _ in xrange(100):  # Change this to a bigger value
        print ('.', end="")
        energy = de.evaluate(f=generate_random_f())
        _max = max(_max, energy)
        _min = min(_min, energy)
    print ("Normalize function _max = {0} _min = {1}".format(_max, _min))
    return _max, _min


def energy(val, _max, _min):
    return (val - _min) / (_max - _min)


def simulated_annealing_for_de(de):

    n = 30
    m = 30
    K_MAX = 1000
    #_max, _min = normalize(de)  # This is going to be costly.
    _min = 0
    _max = de.population_size
    best_f = generate_random_f()
    best_ube = de.evaluate(f=best_f)
    current_energy = best_energy = energy(best_ube, _max, _min)
    k = 1
    for i in xrange(n):
        print()
        print(', {0}, best_ube = {2} , best_f = {3} :{1:.2f},\t'.format(m * i, best_energy, best_ube, best_f), end="")
        for j in range(m):
            next_f = generate_random_f()
            next_ube = de.evaluate(f=next_f)
            next_energy = energy(next_ube, _max, _min)

            if next_energy > best_energy:
                best_ube = next_ube
                best_energy = next_energy
                best_f = next_f
                print('!', end="")

            if next_energy > current_energy:
                current_energy = next_energy
                print("+", end="")

            elif probability(old=current_energy, new=next_energy, k=k/K_MAX) < random.random():
                current_energy = next_energy
                print("?", end="")
            k += 1
            print(".", end="")
    return best_f, best_energy


if __name__ == "__main__":
    de = DifferentialEvolution(population_size=300)
    de.generate_population()
    asdf = simulated_annealing_for_de(de)
    #pdb.set_trace()