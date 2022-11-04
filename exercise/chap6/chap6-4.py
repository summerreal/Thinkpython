#乘方
def is_power(a,b):
    if a%b==0 and is_power(a/b,b):
        return True
  
a=is_power(8,2)
print(a)