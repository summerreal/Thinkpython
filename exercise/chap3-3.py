#练习3-3
   #第一题
print('----------练习3-3------')
def do_twice(f,x,y):
    f(x,y)
    f(x,y)
def do_four(f,x,y):
    do_twice(f,x,y)
    do_twice(f,x,y)
    
def draw(x,y):
    print(x,end=' ')
    print(x,end=' ')
    
    print(y)
def line():
    draw('+ - - - ','+')
    do_four(draw,'|       ','|')
    
def list():
    line()
    line()
    draw('+ - - - ','+')
list()

#第二题
print('----------练习3-3------')
def do_twice(f,x,y):
    f(x,y)
    f(x,y)
def do_four(f,x,y):
    do_twice(f,x,y)
    do_twice(f,x,y)
    
def draw(x,y):
    print(x,end=' ')
    print(x,end=' ')
    print(x,end=' ')
    print(x,end=' ')
    print(y)
def line():
    draw('+ - - - ','+')
    do_four(draw,'|       ','|')
    
def list():
    line()
    line()
    line()
    line()
    draw('+ - - - ','+')
list()

