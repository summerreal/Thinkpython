#打开文件
fin =open('./chap9/words.txt')

for line in fin:
    word =line.strip()
    if len(word)>20:

        print(word)

        '''
    结果：
    counterdemonstrations
    hyperaggressivenesses
    microminiaturizations
        '''