
import string

# def trans(line):#替换特殊字符 !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
#     for i in p:
#         line = line.replace(i,' ')
#     return line

#字典作为计数器集合,计算一个list中每个单词出现的次数。11章
def histogram(t):
    d=dict()
    for c in t:
        d[c] = d.get(c,0) + 1 #接受一个键和一个默认值作为参数。 如果字典中存在该键，则返回对应值；否则返回传入的0值。
    return d

#接受一个字典，值降序输出一个列表
def most_frequent(d):
    t = list()
    for key,value in d.items(): #items返回由多个元组组成的序列，其中每个元组是一个键值对。
        t.append((value,key))
    t.sort()
    t.reverse() #反向列表中元素。
    return t

def makov(fin,n):
    t =[]
    d = {}#单词频率字典
    dd = {} #马尔可夫字典，单词：后缀集合列表
    for line in fin:
        word =line.strip() #字符串方法 strip将字符串开头和末尾的空格删除
        # line = trans(line) ##替换特殊字符 !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
        line= line.split() #无参数，去掉6种whitespace符号： \t\n\r\x0b\x0c
        if line == []:
            continue
        else:
            d1 = histogram(line)
            d.update(d1)
            t.extend(line)
    # print(t)
    for c in range(len(t)-n): #书本单词列表
        if tuple(t[c:c+n]) not in dd:
            dd[tuple(t[c:c+n])] = [t[c+n]]
        else:
             dd[tuple(t[c:c+n])].append(t[c+n])#马尔可夫字典，单词：后缀集合列表
    for qianzhui in dd:
        dd[qianzhui] = histogram(dd[qianzhui]) #计算后缀的单词频率
        dd[qianzhui] = most_frequent(dd[qianzhui] ) # 后缀集合按频率降序排列，
    # print(dd)#马尔科夫分析结果

    return dd

#基于马尔科夫分析生成随机文本
def randomtxt(fin,n):
    dd = makov(fin,n)
    # print(dd)

    txt = 'He was'
    
    for i in range(100):
        start = tuple(txt.split()[-n:])
        # print(start)
        # txt += ' ' + random.choice(dd[start])
        txt += ' ' + dd[start][0][1]
  
    return txt
fin =open('chap13\emma.txt')
text = randomtxt(fin,2)
print(text)