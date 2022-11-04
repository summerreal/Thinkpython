
import turtle
import math
bob = turtle.Turtle()
bob.delay=0.001

def draw(t,length,n):
    if n==0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(angle*2)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)
    
draw(bob,7,7)
turtle.mainloop()