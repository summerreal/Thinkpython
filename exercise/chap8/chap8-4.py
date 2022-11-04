#描述函数功能


def any_lowercase1(s):#判断一个字符串是否包含小写字母，是则返回bool类型：true，否则反回bool类型：false
   
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):#判断一个字符串是否包含小写字母，是则返回字符串：true，否则反回字符串：false
    
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):#判断一个字符串是否包含小写字母，并记录结果
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):#判断一个字符串是否包含小写字母，并返回bool值
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):#判断一个字符串是否包含小写字母，并返回bool值
   
    for c in s:
        if not c.islower():
            return False
    return True