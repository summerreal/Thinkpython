def is_abecedarian(s):
    for i in range(len(s)-1):
        if ord(s[i])>ord(s[i+1]):
            return False
    return True

fin =open('./chap9/words.txt')

count = 0
for line in fin:
    word =line.strip()
    if is_abecedarian(word):
        print(word)
        count += 1
print(count)
   


