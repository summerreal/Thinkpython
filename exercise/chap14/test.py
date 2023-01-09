
import os
from hashlib import md5
import numpy as np

'''walk 返回的是一个三元组(root,dirs,files)。
root 所指的是当前正在遍历的这个文件夹的本身的地址
dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)'''

#搜索一个目录和它的所有子目录中的指定后缀fileformat，
#返回一个列表，列表中包含所有的有给定后缀（例如.mp3）的文件的完整路径
def allfile(direct,fileformat):
    pathlist = []
    filenamelist = []
    n = len(fileformat)
    # print(n)
    #walk通过在目录树中游走输出在目录中的文件名，
    ##topdown可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。
    for root, dirs, files in os.walk(direct):
        for name in files:
            # print(name)
            if name.endswith(fileformat): #检索出该类型的文件
                # print(name,fileformat)
                if name in filenamelist: #检索出相同文件名的文件，并打印
                    print(os.path.join(root, name))
                else:
                    filenamelist.append(name)
                    path = os.path.join(root, name)                
                    pathlist.append(path)
                    # print(os.path.join(root, name))
        
        # for name in dirs:
        #     print(os.path.join(root, name))
    return pathlist

#传入一个文件名，返回它的文件内容的校验和
def checksum(filename):
    t = []
    fin = open(filename)
    for line in fin:
        t.append(line)
    m = md5()
    m.update(str(t).encode(encoding='utf8'))
    mval = m.hexdigest()
    return mval
 

def recur(direct,fileformat):
    t = allfile(direct,fileformat) #获取目录的所有文件的路径列表
    # print(t)
    t1 =[]
    for filename in t:
        t1.append(checksum(filename))#获取文件对应的哈希列表
    # print('%s目录中的重复文件路径为有：'%direct)
    for i in range(len(t1)):
        if t1.count(t1[i])>1:
            print(t[i]) #输出重复文件

# fin = open('D:\summer\exercise\chap14\emma.txt')
fileformat = '.txt' #要检索的文件类型
direct = cwd = os.getcwd() #要检索的目录，以当前目录为例
recur(direct,fileformat)