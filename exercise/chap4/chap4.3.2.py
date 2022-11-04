#练习4.3.2
#第2题
import turtle
bob = turtle.Turtle()

#定义画正方形函数
def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
#调用该函数
square(bob,200)