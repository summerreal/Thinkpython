#二分法查找单词
def in_bisect(t,letter):
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
        
def one_append():
    t=[]
    fin =open('./chap9/words.txt')
    for line in fin:
        #print(line)
        word =line.strip()
        t.append(word)
    return t
t=sorted(one_append())

ans = in_bisect(t,'aal')
print(ans)

