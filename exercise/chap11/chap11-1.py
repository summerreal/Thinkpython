#检查字符是否在字典中,
def readtxt(): #获得words.txt列表，存储在列表t
    d=dict()
    i=0
    fin =open('./chap9/words.txt')
    data = fin.read().splitlines()
    for line in data:
        #print(line)
        i=i+1
        d[line]=i
        #d[line[:-2]]=i
    fin.close()
    return d
jud='zymurgy'
if  jud in readtxt():
    print('找到啦')
else:
    print('什么都没有')