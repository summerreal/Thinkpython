#chap5-3
#判断三角形

def is_triangle(a,b,c):
    if a>=b+c or b>=c+a or c>=a+b:
        print('No')
    else:
        print('Yes')

a,b,c = map(int,input('请输入三根木棍的长度,空格隔开：').split())
is_triangle(a,b,c)