#练习4-3
#第1题函数画雨伞
#l:伞骨长度，n:伞骨（三角形）个数

import turtle
import math
bob = turtle.Turtle()
bob.delay=0.01

#定义画已知角度和边长的等腰三角形函数，r_length ：等腰边长，n：n个三角形，angle:角度
def triangle(r_length,n):
    t = bob
    angle =180-(180-360.0/n)/2
    length =2* r_length*math.sin(math.pi/n)
    for i in range(n):
        t.fd(r_length)
        t.lt(angle)
        t.fd(length)
        t.lt(angle)
        t.fd(r_length)
        t.lt(180)
#输入伞骨长度,伞骨数量，
triangle(100,9)

turtle.exitonclick()