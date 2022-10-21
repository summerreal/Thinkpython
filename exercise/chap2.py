#chap2
#练习2-2
#第一题
import math
r=5
s =4/3*r**3*math.pi
print('半径为{}的球体体积为{}'.format(r,s))

#第二题
total=24.95*0.6*60+3+0.75*(60-1)
print('60本书的总价是{}美元'.format(total))

#第三题
totalseconds = (6*60+10)*1.6*2 + (4*60+30)*4.8
x=6+1 #小时
y=(52+int(totalseconds/60))%60 #分钟
z=0 + totalseconds%60

print('回家吃早餐的时间是{}时{}分{}秒'.format(x,y,z))