
#回文
def first (word):
    return word[0]

def last (word):
    return word[-1]

def middle (word):
    return word[1:-1]

# print(middle('gh'))  #输出为空
# print(middle('')) 

def is_palindrome(s):
    if len(s)<=1:
        return True
    if first(s)!=last(s):
        return False
    return is_palindrome(middle(s))

print(is_palindrome('esdfg'))