def has_duplicates(t):
    t=sorted(t)
    for i in range(len(t)-1):
        if t[i]==t[i+1]:
            return True

t=[1,2,2,3]
print(has_duplicates(t))