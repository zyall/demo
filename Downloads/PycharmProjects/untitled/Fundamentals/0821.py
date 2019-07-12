#coding=utf-8
'''
l1=['Hello','World', 18,None,'Apple']
l=[]
for i in l1:
    if isinstance(i,str) is True:  # isinstance函数可以判断一个变量是不是字符串
        l.append(i)
l2 =[s.lower() for s in l] #把list中的所有的字符串变成小写
print(l2)
'''

def fib(max):
    n,a,b=0,0,1
    while n < max:
        yield b  #generator生成器
        a,b=b,a+b
        n=n+1
    return 'done'
'''
for n in fib(6):
    print(n)
'''
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break














