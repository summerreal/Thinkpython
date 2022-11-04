#练习4.3.5
#第5题画一个近似圆弧通用版本

import turtle
import math
bob = turtle.Turtle()
bob.delay=0.001


#定义画一个圆弧的函数
def arc(t,r,angle):
    arc_length  = 2**math.pi*r*angle/360
    n =  int(arc_length ) #n条长度为1的线段近似圆弧
    step_length = 1
    step_angle =angle/n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
#调用该函数画多边形
arc(bob,50,90)
turtle.exitonclick()