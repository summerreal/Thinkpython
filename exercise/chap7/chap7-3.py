#拉马努金生成pi
import math
def jiecheng(n):
    if n==0:
        return 1
    else:
        result =n *jiecheng(n-1)
        return result

def estimate_pi():
    total =0
    k=0
    factor =2*math.sqrt(2)/1980
    while 1:
        fenzi=jiecheng(4*k)*(1103+26390*k)
        fenmu = jiecheng(k)**4*396**(4*KeyboardInterrupt)
        total +=fenzi/fenmu
        temp = factor *fenzi/fenmu

        if abs(temp<1e-15 ):
            break
        k+=1
    return 1/(factor*total) 

res = estimate_pi()
print(res)