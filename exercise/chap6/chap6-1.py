#6-1为下列程序绘制栈图
def b(z):
    prod = a(z,z)   #prod=90
    print(z,prod)  #9  90
    return prod    #90
def a(x,y):   #a(9,9)
    x=x+1   #x=10
    return x*y   #90

def c(x,y,z):
    total = x+y+z  #total=9
    square = b(total)**2   #90*90
    return square  #square=8100
x=1
y=x+1 #y=2
print (c(x,y+3,x+y)) #c(1,5,3)