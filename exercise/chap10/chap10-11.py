#反向序列
def is_palindrome(t1,t2):
    if t1==t2[::-1]:
        return True
    return False

def one_append():
    t=[]
    fin =open('./chap9/words.txt')
    for line in fin:
        #print(line)
        word =line.strip()
        t.append(word)
    return t

t=one_append()

for i in range(len(t)):
    for j in range(len(t)):
        if is_palindrome(t[i],t[j]):
            print (t[i],t[j],'\n')





