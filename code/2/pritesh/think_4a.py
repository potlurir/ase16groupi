from swampy.TurtleWorld import *
from math import pi


def move(t, x, y):
    t.pu()
    t.x = x
    t.y = y
    t.pd()


def square(t, length=100):
    """ Draw a square.
    :param t: A turtle that shall draw
    :param length: Side length of the square
    :return: None
    """
    for _ in range(4):
        t.fd(length)
        t.lt()


def polyline(t, length=100, number_of_sides=4, angle=360):
    """ Helper function to draw arcs/polygon/circle.
    :param t: the turtle object
    :param length: side length
    :param number_of_sides:
    :param angle: Angle an arc makes at center
    :return: None
    """
    for _ in range(number_of_sides):
        t.fd(length)
        t.lt(angle/float(number_of_sides))


def polygon(t, length=100, number_of_sides=4):
    polyline(t, length, number_of_sides, 360)


def circle(t, radius):
    arc(t, radius, 360)


def arc(t, radius, angle):
    side_count = 1000
    arc_len = (angle/360.0) * 2 * pi * radius
    side_len = arc_len / side_count
    print (side_len, arc_len)
    polyline(t, side_len, side_count, angle)


def petal(t, radius, angle):
    for _ in range(2):
        arc(t, radius, angle)
        t.lt(180 - angle)


def flower(t, n, radius, angle):
    for _ in range(n):
        petal(t, radius, angle)
        t.lt(360.0/n)

"""
arc(bob, 50, 270)
square(bob, 200)
polygon(bob, 5, 80)
circle(bob, 20)
arc(bob, 100, 180)
arc(bob, 100, 60)
flower(bob, 12, 100, 10)
flower(bob, 6, 200, 60)
"""


if __name__ == "__main__":
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.0001

    # Function args used from code sample in book
    move(bob, -100, 0)
    flower(bob, 7, 60, 60)

    move(bob, bob.get_x()+ 100, 0)
    flower(bob, 10, 40, 80)

    move(bob, bob.get_x() + 200, bob.get_y() - 200)
    flower(bob, 20, 140, 20)
    wait_for_user()

