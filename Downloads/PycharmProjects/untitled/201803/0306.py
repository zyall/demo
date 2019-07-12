# coding:utf-8

#变量重新赋值
a=1
a="222"
print(a)
#计算1-10的整数求和
b=[1,2,3,4,5,6,7,8,9,10]
s=0
for i in b:
    s=s+i
print(s)
#多个变量赋值
a=b=c=1
print(a,b,c)
d,e,f=1,2,"hello"
print(d,e,f)
#字符串操作
s="hello"
a="world"
print(s+a)
print(s*3)
#字符串的切片
s1="hello world!"
print(s1[1:4])  #从1-4
print(s1[4:])   #从4开始往后切
print(s1[:4])   #从前面的开始切到4
print

l=[3,2,1,9,10,78,6]
l.sort()
print(l)

s=0
for i in list(range(11)):
    s+=i
print(s)