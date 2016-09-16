from __future__ import print_function
import math
import random

    
def find_max_f1_f2(x):
    return pow(x,2) + pow(x-2, 2)
    
def find_schaffer_max_min():
    max = -float("inf")
    min = +float("inf")
    for i in range(10000):
        e = find_max_f1_f2(random.randint(-100000, 100000))
        max = e if e > max else max
        min = e if e < min else min
    return max, min

print(find_schaffer_max_min())
    
SC_MAX, SC_MIN = find_schaffer_max_min()
K_MAX = 1000.0

def schaffer(x):
    return (pow(x,2) + pow((x-2), 2) - SC_MIN) / float(SC_MAX - SC_MIN)
    
def propability(old, new, k):
    return math.exp((old - new)/float(k))

def simulated_annealing():
    seed = random.randint(0,100)
    random.seed(seed)
    s = random.randint(-100000, 100000)  # initial state
    e = schaffer(s)  # Initial energy
    sb = s  # best solution
    eb = e  # lowest energy
    n = 30  # Number of cycles
    m = 25  # number of trials per cycle
    k = 1
    print(s, e)
    for i in range(n):
        print()
        print(', {0}, :{1:.2f},\t'.format(25 * i, e), end="")
        for j in range(m):
            sn = random.randint(-100000, 100000)
            en = schaffer(sn)
            if en < eb:  # We got the best yet
                sb, eb = sn , en
                print ("!", end="")
                
            if en < e:  # we got someone better, take it :) 
                s, e = sn, en
                print("+", end="")
            elif propability(e, en, k/K_MAX) < random.random(): # We are making a crazy decision
                s = sn
                e = en 
                print("?", end="")
            k += 1    
            print(".", end="")
    return seed, sb, eb, n, m, 

seed, sb, e, n, m = simulated_annealing()
print("\nseed = {0}, sb= {4}, e={1}, \nnumber of cycles = {2}, number of trials per cycle = {3}".format(seed, e, n, m, sb))
