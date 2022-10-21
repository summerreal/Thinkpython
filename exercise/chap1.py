#chap1练习1-1
#第一题：漏掉括号会提示语法错误：SyntaxError： unexpected EOF while parsing
#第二题：漏掉字符串的引号会提示语法错误：SyntaxError：EOL while scanning string literal
#第三题：数字前加+号，程序会继续运行。2++2输出结果为 4
#第四题：02湖提示语法错误：invalid token

#chap1练习1-2
#第一题：
seconds=42*60+42
print("一共有{}秒".format(seconds))
#第二题：
m=10/1.61
print("10千米一共有{}英里".format(m))
#第三题
seconds=42*60+42
km=10
hours = 42/60+42/60/60
minutes=int(seconds/10/60)
oneksc = seconds/10.0%60
average = km/hours
print("跑一千米需要{}分钟和{}秒，{}千米每小时".format(minutes,oneksc,average))

#课堂练习小作业
import math
print ("This is s code cell ...and Pi is =",math.pi)
print("hello world")

x = 1
y = +2
x,y=y,x
print("After swapping")
print ('x = ' ,x)
print ('y = ' ,y)
print(2++2)
