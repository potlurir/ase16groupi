# Assuming Non Leap Year.
import random


def has_duplicates(lst):
    return len(set(lst)) != len(lst)

# Got this from reading random function docs
def randomBirthdays(n):
    return [random.randint(0, 365) for i in xrange(0, n)] 

print has_duplicates(randomBirthdays(100))
print has_duplicates(randomBirthdays(5))

# Had to see the solution because I didn't understand
# how many samples I can take.
def probability():
    count = 0
    # I am assuming 10000 samples
    for i in xrange(0, 10000):
        if has_duplicates(randomBirthdays(23)):
            count += 1
    return float(count)/10000

print probability()
