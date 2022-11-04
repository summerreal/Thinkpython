
def is_palindrome(s1:int,s2:int):
    s1=str(s1)    
    s2=str(s2%100)
    if s1==s2[::-1]:
        return True
    return False

for my_age in range(1,100):  #我的第一次回文年龄范围
    for k in  range(9,70): #年龄差距
        count=0
        for year in range(140): #寿命上上限设置
            me = my_age+year
            mo = my_age+year+k
            
            if is_palindrome(me,mo):
                count +=1
                
                if count==6:
                   age_now=me
                if count==8:
                    print('我现在的年龄是：',age_now)
                    break

#
