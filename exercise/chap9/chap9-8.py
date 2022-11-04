#che

def is_palindrome(s):
    if s==s[::-1]:
        return True
    return False

for i in range(10**5,10**6):
    s=str(i)
    s1=s[2:]

    if is_palindrome(s1):
        s2=str(int(s)+1)
        if is_palindrome(s2[1:]):
            s3=str(int(s2)+1)
            if is_palindrome(s3[1:5]):
                s4=str(int(s3)+1)
                if is_palindrome(s4):
                    print(s)
        


