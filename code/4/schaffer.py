from __future__ import print_function
import argparse
import math
import random

#---------------------------------------------------------------
# command to run: $ python schaffer.py --n 1000 --m 50 --seed 20
# n, m and seed are optional arguments
parser = argparse.ArgumentParser()
parser.add_argument("--n", help="Number of cycles. Default is 30", type=int)
parser.add_argument("--m", help="Number of trials per cycle. Default is 25", type=int)
parser.add_argument("--seed", help="A seed for random generator. Default is a random int between 1 and 100", type=int)
#---------------------------------------------------------------    

def find_max_f1_f2(x):
    return pow(x,2) + pow(x-2, 2)
    
def find_schaffer_max_min():
    """Calculate the maximum and minimum of (F1 + F2)
    
    A baseline study where you run the Schaffer 10000 times to find the min 
    and max values for (f1 + f2). This is needed to normalize the shaffer 
    objective function value in 0..1.
    """
    max = -float("inf")
    min = +float("inf")
    for i in range(10000):
        e = find_max_f1_f2(random.randint(-100000, 100000))
        max = e if e > max else max
        min = e if e < min else min
    return max, min

#print(find_schaffer_max_min())
    
SC_MAX, SC_MIN = find_schaffer_max_min()
K_MAX = 1000.0

def schaffer(x):
    "The schaffer objective function"
    return (pow(x,2) + pow((x-2), 2) - SC_MIN) / float(SC_MAX - SC_MIN)
    
def probability(old, new, k):
    return math.exp((old - new)/float(k))

def simulated_annealing(n, m, seed):
    # n is Number of cycles
    # m is number of trials per cycle
    random.seed(seed)
    s = random.randint(-100000, 100000)  # initial state
    e = schaffer(s)  # Initial energy
    sb = s  # best solution
    eb = e  # lowest energy
    k = 1
    print("Initial State: {0}\nInitial Energy: {1} \n".format(s, e))
    print("\nNote: ")
    print("Each line represents a cycle of {0} trials. \nEach trial is represented by a full stop i.e. '.'".format(m))
    print("Additionally: \n'?' means we picked a state that was not as good as the present state. i.e 'A drunken decision'")
    print("'+' means we picked a state that was better than the current one.")
    print("'!' means we picked a state that is the best among the states encounterd yet.")
    print("For larger n and m, the number of ? printed should decrease.")
    for i in range(n):
        print()
        print(', {0}, :{1:.2f},\t'.format(m * i, e), end="")
        for j in range(m):
            sn = random.randint(-100000, 100000)
            en = schaffer(sn)
            if en < eb:  # We got the best yet
                sb, eb = sn , en
                print ("!", end="")
                
            if en < e:  # we got someone better, take it :) 
                s, e = sn, en
                print("+", end="")
            elif probability(e, en, k/K_MAX) < random.random(): # We are making a crazy decision
                s = sn
                e = en 
                print("?", end="")
            k += 1    
            print(".", end="")
    return sb, eb 

    
if __name__ == "__main__":
    args = parser.parse_args()
    seed = args.seed if args.seed else random.randint(0,100)
    n = 30 if args.n is None else args.n
    m = args.m if args.m else 25

    sb, e= simulated_annealing(n, m, seed)
    print("\nseed = {0}, sb= {4}, e={1}, \nnumber of cycles = {2}, number of trials per cycle = {3}".format(seed, e, n, m, sb))
