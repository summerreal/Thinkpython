#ackerman函数实现，递归
 
def ack(m:int,n:int):
    if m==0:
        return n+1
    if n==0 and m>0:
        return ack(m-1,1)
    
    return ack(m-1,ack(m,n-1))

print(ack(3,4))