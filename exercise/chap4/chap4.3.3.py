#练习4.3.3
#第3题
import turtle
bob = turtle.Turtle()
bob.delay=0.1

#定义画n边形函数
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
#调用该函数画多边形
polygon(bob,100,7)