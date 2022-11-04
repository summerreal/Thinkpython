#互斥锁

def one_append(): #获得words.txt列表，存储在列表t
    t=[]
    fin =open('./chap9/words.txt')
    for line in fin:
        #print(line)
        word =line.strip()
        t.append(word)
    return t
def in_bisect(t,letter):  #查找单词letter是否在列表t中
    a=0
    b=len(t)
    i=len(t)//2
    if t[i]==letter:
        return True
    if letter in t[a:int((a+b)/2)]:
        b=(a+b)//2
        return in_bisect(t[a:b],letter)
    elif letter in t[int((a+b)/2):b]:
        a=(a+b)//2
        return in_bisect(t[a:b],letter)
    

def comp(t,word): #word组成的单词，判断拆分后的两个是否在列表t中
    even=word[::2]
    odd = word[1::2]
    if in_bisect(t,even) and in_bisect(t,odd):
        print(even,odd)
        #return even,odd
    
t=one_append()

for i in t:
    comp(t,i)
    




