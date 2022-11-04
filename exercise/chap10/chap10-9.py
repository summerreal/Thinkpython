import time

def one_append():
    t=[]
    fin =open('./chap9/words.txt')
    for line in fin:
        #print(line)
        word =line.strip()
        t.append(word)
    return t
def two_add():
    t=[]
    fin =open('./chap9/words.txt')
    for line in fin:
       
        word =line.strip()
        t+=word
    return t


start_time1=time.time()
t=one_append()
print(t)
t1=time.time()-start_time1


start_time2=time.time()
t=two_add()
t2=time.time()-start_time2

print('两个方法运行的时间分别为：append：%d秒，+号的运行时间围殴：%d秒'%(t1,t2))