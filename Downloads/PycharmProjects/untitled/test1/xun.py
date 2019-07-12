#a=[1,2,<=,>=,<>,=,取值，不取值]
#b=['<','>','<=','>=','<>','=','取值','不取值']
'''
import itertools

a =['<','>','<=','>=','<>','=','取值','不取值']

c = itertools.combinations(a,2)

for i in c:
    print(i)


wifi=[开，关]

应用=[打开qq，打电话]


这两个全交组合生成用例
会生成4个用例

第一个用例  #wifi 开  #应用 打开qq
第二个用例  #wifi 关  #应用 打开qq

第三个用例  #wifi 开  #应用 打电话
第四个用例  #wifi 关  #应用 打电话


如果我添加了约束规则：
if wifi 取值 关  then 应用 取值  打电话

那只生成三条用例

第一个用例  #wifi 开  #应用 打开qq
第四个用例  #wifi 关  #应用 打电话

#例题1
i = int(input('净利润:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        #print((i - arr[idx]) * rat[idx])
        i = arr[idx]
print(r)


a=[1, 2, 3, 4] # a可以取值的列表
b=["a", "b", "c", "d"]# b可以取值的列表
rule = ["1a","2b", "3c", "4d"] # 约束规则
comb = []
for x in a:
    for y in b:
        comb.append(str(x)+str(y))
for i in rule:
    if i not in comb:
        comb.remove(i)

print(comb)


rule=str(input("输入约束规则："))
a=[1, 2, 3, 4] # a可以取值的列表
b=["a", "b", "c", "d"]# b可以取值的列表
comb = []
for x in a:
    for y in b:
        comb.append(str(x)+str(y))
for i in comb:
    if i not in rule:
        comb.remove(i)

print(comb)
'''
#思路：
#1.先全交生成所有组合  comb

#2.约束规则  rule
#删除不符合约束规则的组合
#not in rule
#comb.remove(i)
#rule=str(input("输入约束规则："))

#coding=utf-8

#约束规则筛选出符合条件的取值，生成一个文件，转成list




#读取约束规则list生成用例list，将用例list转成文件
#比对



a=['1','2','3','4'] # a可以取值的列表
b=['a','b','c','d']# b可以取值的列表
rule=[] #约束规则
condition=[]  #约束条件可以取值的列表
result=[]
comb=[]  #用例结果
fo=open("/Users/zq1/Downloads/condition.txt","r")
y=open("/Users/zq1/Downloads/result.txt.txt","r+")
#line=fo.readlines()
for line1 in fo.readlines():
    line1 = line1.strip('\n')
    condition.append(line1)
for line2 in y.readlines():
    line2 = line2.strip('\n')
    result.append(line2)
for k in range(5):
    for i in a:
        if i in condition:
            a.remove(i)
for w in range(5):
    for j in b:
        if j in result:
            b.remove(j)
for i in condition:
    for j in result:
        rule.append(str(i) + str(j))
print(rule)
for i in a:
    for j in b:
        comb.append(str(i) + str(j))
print(rule + comb)



