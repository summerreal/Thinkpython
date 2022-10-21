#第三章
#练习3-1

def right_justify(s):
    print(' '*(70-len(s)))
    print(s)

right_justify('mouty')

#练习3-2
#第一题
def do_twice(f):
    f()
    f()
    
def print_spam():
    print('spam')
    
do_twice(print_spam)
print('----------答案分隔线-------------')

#第二题
def do_twice(f,x):
    f(x)
    f(x)
    
def print_spam(x):
    print(x)
    
do_twice(print_spam,'spam')
print('----------答案分隔线---------')
      
#第三题定义函数
def print_twice(bruce):
    print(bruce)
    print(bruce)
print('----------答案分隔线------')
#第四题
do_twice(print_twice,'spam')
print('----------答案分隔线------')


#第五题
def do_twice(f,x):
    f(x)
    f(x)
def do_four(f,x):
    do_twice(f,x)
    do_twice(f,x)
    
