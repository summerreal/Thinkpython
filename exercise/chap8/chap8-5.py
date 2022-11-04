#凯撒密码

def rotate_word(s,n):
    res=''
    for i in s:
        if s.islower():
            start = ord('a')
        elif s.isupper():
            start =ord('A')
        else:
            start=i


        m=(ord(i)-start+n)%26+start
        res +=chr(m)
        

    return res

a=rotate_word('cheer',7)
print(a)
