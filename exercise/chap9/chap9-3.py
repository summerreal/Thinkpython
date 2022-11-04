#没有e
#打开文件
fin =open('./chap9/words.txt')

def avoid():
    str_avoid=input('输入包含禁止字母的字符串')

    count=0
    for line in fin:
        for letter in line:
            if letter in str_avoid:
                word =line.strip()
                print(word)
                count+=1
                break
    print(count)
avoid()   

