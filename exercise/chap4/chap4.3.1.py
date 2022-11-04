#练习4.3.1
#第一题
import turtle
bob = turtle.Turtle()

#定义画正方形函数
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
#调用该函数
square(bob)