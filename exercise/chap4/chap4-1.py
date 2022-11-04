#练习4-2
#第1题画圆

import turtle
import math
bob = turtle.Turtle()
bob.delay=0.01

#定义画n边形函数，length ：画线长度，n：n边形，angle:弧度
def polygon(t,length,n,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#弧线，画一个弧，t:bob,r:弧半径 , angle :弧度
def arc(t,length,angle):
    m = int(length)  
    step = 2*math.pi*length/m  #弧线分成m份
    step_angle = angle/m
    polygon(t,step,m,step_angle)

#定义函数：花瓣的长度和数量 
def flower(l,nn):
    
    #奇数花瓣没有重合
    if nn%2 ==1:
        for i in range(nn):
            arc_r = l/(2*math.sin(math.pi/nn))
            angle = 360/nn
            arc_length = 360/nn*arc_r
            arc(bob,arc_r,angle)
            
        
    
#输入花瓣的长度和数量    
flower(10,9)
turtle.exitonclick()