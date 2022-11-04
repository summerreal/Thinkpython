#chap5-2
#费马大定理

#定义check函数，条件里加上n>2
def check_fermat(a,b,c,n):
    if n>2 and(a**n + b**n == c**n):
        print('天哪，费马弄错了！')
    else:
        print('不，那样不行')

#输入多个数，同时转为整数型
a,b,c,n = map(int,input('请输入a,b,c,n,空格隔开').split())

#调用函数
check_fermat(a,b,c,n)
