#车迷天下
def find_triple():
    fin =open('./chap9/words.txt')
    for line in fin:
         word =line.strip()
         i=0
         count=0
         while i <len(word)-1:
            if word[i]==word[i+1]:
                count +=1
                if count ==3:
                    print(word)
                i=i+2
            else:
                i=i+1
                count =0
 
find_triple()

'''
结果
bookkeeper
bookkeepers
bookkeeping
bookkeepings
'''