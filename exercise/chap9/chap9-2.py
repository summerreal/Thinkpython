#禁止单词


fin =open('./chap9/words.txt')

def has_no_e(s):
    for j in s:
        if j=='e':
            return 0
    return 1
k=0
k1=0
for line in fin:
    k+=1
    word =line.strip()
    if has_no_e(word):
        print(word)
        k1+=1
print(k1/k*100,'%')

