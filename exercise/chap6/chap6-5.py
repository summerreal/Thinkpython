#最大公约数

def gcd(a,b):
    if b==0:
        return a
    r=a%b
    return gcd(b,r)

a=gcd(4,8)
print(a)
