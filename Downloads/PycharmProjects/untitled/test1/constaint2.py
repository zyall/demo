#coding=utf-8
a = ["开wifi", "关wifi", "电量30", "电量40", "电量50", "充电状态", "非充电状态", "飞行模式", "3G网络", "4G网络"] # a可以取值的列表
b = ["使用QQ", "打电话", "使用浏览器", "使用文本", "使用计算器"]  # b可以取值的列表
condtion=['开wifi']
rule=[]
l=[m + n for m in a for n in b]
for i in range(10):
    for x in a:
        if i in condtion:
            a.remove()


print(l)




'''
a=[1,2,3,4] # a可以取值的列表
b=['a','b','c','d']# b可以取值的列表
condition=['电量30','电量40','开wifi']  #约束条件可以取值的列表
result.txt=['使用QQ',"打电话"]     #约束结果可以取值的列表
rule=['电量30使用QQ', '电量40打电话', '开wifi使用QQ',"电量30打电话"]
comb=[] #脚本结果
for k in range(10):
    for i in a:
        if i in condition:
            a.remove(i)
for w in range(10):
    for j in b:
        if j in result.txt:
            b.remove(j)
    for x in condition:
        for y in result.txt:
            rule.append(str(x)+str(y))
for i in a:
    for j in b:
        comb.append(str(i) + str(j))
fileObject = open('/Users/zq1/Downloads/sampleList.txt', 'w')
for idx in (rule+comb):
        fileObject.write(idx)
        fileObject.write('\n')
fileObject.close()
print(rule)
print(rule+comb)
'''