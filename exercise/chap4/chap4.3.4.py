#练习4.3.4
#第4题画一个近似圆

import turtle
import math
bob = turtle.Turtle()
bob.delay=0.001

#定义画n边形函数
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
def circle(t,r):
    n= int(math.pi*r) #定义每条边长为1，一共有2pi*r条长为1的线段，近似于一个圆
    length = 1
    polygon(bob,length,n)
#调用该函数画多边形
circle(bob,130)