
def uses_all(letter,s):
    
    for c in s:
        if c not in letter:
            return False
    return True



a=uses_all('hoe alfalfa','aeiou')
print(a)

##还没有写完的作业