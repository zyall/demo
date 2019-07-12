#coding=utf-8
'''
#杨辉三角

def triangles():
    l=[1]
    while True:
        yield l
        l.append(0)
        #print(l)
        l=[l[i-1]+l[i] for i in range(len(l))]
n=0
for t in triangles():
    print(t)
    n+=1
    if n==10:
        break

#如何生成指定长度的字符串
import random

#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
l=list(range(1,5))
for i in l:
    for j in l:
        for k in l:
            if (i!=j) and (j!=k) and (i!=k):
                print(i,j,k)
'''
#企业发放的奖金根据利润提成。
#利润(I)低于或等于10万元时，奖金可提10%；
#利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%
#20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
#60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？



























