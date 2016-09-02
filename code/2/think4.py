from swampy.TurtleWorld import TurtleWorld, Turtle, fd, lt, wait_for_user
import math


def square(length):
    for i in xrange(0, 4):
        fd(t, length)
        lt(t)

def polygon(n, length):
    angle = 360.0/n
    for i in xrange(0, n):
        fd(t, length)
        lt(t, angle)



world = TurtleWorld()
t = Turtle()

# square(100)
polygon(5, 100)
wait_for_user()