#班级重复的生日

import random

n=23
count =0
for i in range(100000):

    t=[]
    for j in range(n):
        t.append(random.randint(1,365))
        
    t=sorted(t)
    for j in range(n-1):
        if t[j]==t[j+1]:
            count +=1
            break
p=count/100000
print(p)
