def is_anagram(l1,l2):
    if l1==sorted(l2):
        return True
    
t1=[1,2,3]
t2=[1,3,2]
print(is_anagram(t1,t2))

