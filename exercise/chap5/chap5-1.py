#chap5-1
#time时间戳计算

import time

t=time.time()   #获得当前时间戳，float秒数
hour =(t//3600)%24+8  #计算的时间不对
minutes =t//60%60
second=t%60
day = t/60/60//24
print('当前时间戳为{}，可转换为{}时{}分{}秒，从纪元到现在的天数为：{}天'.format(t,hour,minutes,second,day))

