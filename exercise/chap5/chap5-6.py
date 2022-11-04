#chap5-6
#科赫曲线

import turtle
import math
bob = turtle.Turtle()
bob.delay=0.001
def koch(t,length,n):
    if n==0:
        t.fd(length)
    else:
        koch(t,length/3,n-1)
        t.lt(60)
        koch(t,length/3,n-1)
        
        t.rt(120)
        koch(t,length/3,n-1)
    
        t.lt(60)
        koch(t,length/3,n-1)
   

for i in range(3):
    koch(bob,150,3)
    bob.rt(120)

turtle.exitonclick() 