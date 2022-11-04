#练习4-1
#第一题函数画花朵


from __future__ import print_function, division

import math
import turtle
bob = turtle.Turtle()
bob.delay=0.0001


def square(t, length):
    """Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, n, step_length, step_angle)



def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)



    # bob = turtle.Turtle()

    # # draw a circle centered on the origin
    # radius = 100
    # bob.pu()
    # bob.fd(radius)
    # bob.lt(90)
    # bob.pd()
    # circle(bob, radius)

#奇数花瓣花朵
def flower1(l,m):
    '''
    l:花瓣长度
    m：花瓣数量
    '''
    arc_angle=360/m
    arc_angle2 = 2*math.pi/m
    arc_r = l/2/math.sin(arc_angle2/2)
    arc_length = arc_angle2*arc_r
    turn_angle = 180-arc_angle
    for i in range(m):
        arc(bob,arc_r,arc_angle)
        bob.lt(turn_angle)
        arc(bob,arc_r,arc_angle)
        bob.lt(180)

def flower2(l,m):
    m=int(m/2)
    '''
    l:花瓣长度
    m：花瓣数量
    '''
    arc_angle=360/m
    arc_angle2 = 2*math.pi/m
    arc_r = l/2/math.sin(arc_angle2/2)
    arc_length = arc_angle2*arc_r
    turn_angle = 180-arc_angle
    for i in range(m):
        arc(bob,arc_r,arc_angle)
        bob.lt(turn_angle)
        arc(bob,arc_r,arc_angle)
        bob.lt(180)
    bob.lt(360/2/m)
    for j in range(m):
        arc(bob,arc_r,arc_angle)
        bob.lt(turn_angle)
        arc(bob,arc_r,arc_angle)
        bob.lt(180)
def flower(l,num):
    if num%2==1:
        flower1(l,num)
    else:
        flower2(l,num)

flower(100,12)
    # wait for the user to close the window
turtle.mainloop()