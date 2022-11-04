#平方根
import math
def square_root(a):
    epsilon=0.0000001
    x=a
    y=(x+a/x)/2
    while 1:
        y=(x+a/x)/2
        if abs(y-x)<epsilon:
            break
        x=y
    return x

print("a\t",'mysqrt(a)\t','math.sqrt(a)\t','diff\t')
print("-\t",'--------\t','-------------\t','----\t')
for i in range (1,9):
    print(float(i),'\t',square_root(i),math.sqrt(i),'\t',square_root(i)-math.sqrt(i),'\n')
    


#a=square_root(4)
#print(a)


