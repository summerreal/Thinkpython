#chap5-4
#写注释
'''
这是一个计算首项为s,公差为1的n项的等差数列的和
'''

def recurse(n,s):
    if n==0:
        print(s)
    else:
        recurse(n-1,n+s)
recurse(3,0)
#如果参数为：（-1，0）无线递归导致错误

