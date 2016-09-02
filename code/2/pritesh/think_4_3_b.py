from math import cos
from math import radians
from swampy.TurtleWorld import *
from think_4a import move
from think_4a import polygon
# Exercise 4 http://www.greenteapress.com/thinkpython/html/thinkpython005.html#toc51


def polygon_flowers(t, length, n):
    polygon(t, length, n)
    # p is distance between the center of polygon to its vertices
    p = length/(2 * cos(radians(90 - 180.0/n)))
    t.lt((90 - 180.0/n))
    t.fd(p)
    # x and y are the coordinates of the center of the polygon
    x = t.get_x()
    y = t.get_y()
    t.lt(180)
    for _ in range(n-1):
        t.lt(360/n)
        t.fd(p)
        move(t, x, y)

if __name__ == "__main__":
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.01
    move(bob, -100, 0)
    polygon_flowers(bob, length=50, n=5)
    move(bob, bob.get_x() + 150, bob.get_y())
    polygon_flowers(bob, length=50, n=6)
    move(bob, bob.get_x() + 150, bob.get_y())
    polygon_flowers(bob, length=50, n=7)
    wait_for_user()