#反转字典
def invert_dict(d):
    inverse = {}
    for key in d:
        temp = d[key]
        inverse.setdefault(temp,[]).append(key)
    return inverse

d={'a':1,'b':2,'c':3}
print(d)
inverse=invert_dict(d)
print(inverse)
for key in inverse:
    print(key,inverse[key])