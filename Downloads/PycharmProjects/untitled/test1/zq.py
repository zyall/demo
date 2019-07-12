#coding=utf-8
a = ["开wifi", "关wifi", "电量30", "电量40", "电量50", "充电状态", "非充电状态", "飞行模式", "3G网络", "4G网络"]  # a可以取值的列表
b = ["使用QQ", "打电话", "使用浏览器", "使用文本", "使用计算器"]  # b可以取值的列表
#a=[1,2,3,4] # a可以取值的列表
#b=['a','b','c','d']# b可以取值的列表
condition=['电量30','电量40','开wifi']  #约束条件可以取值的列表
result=['使用QQ',"打电话"]     #约束结果可以取值的列表
sh=[] #脚本结果
rule=['电量30使用QQ', '电量40打电话', '开wifi使用QQ',"电量30打电话"]
'''
c_file=open("/Users/zq1/Downloads/condition.txt","r")
r_file=open("/Users/zq1/Downloads/result.txt.txt","r+")
line=fo.readlines()
for x in c_file.readlines():
    x =str(x.strip('\n'))
    condition.append(x)
for y in r_file.readlines():
    y =y.strip('\n')
    result.txt.append(y)
'''
for k in range(10):
    for i in a:
        if i in condition:
            a.remove(i)
for w in range(10):
    for j in b:
        if j in result:
            b.remove(j)
for i in a:
    for j in b:
        sh.append(str(i) + str(j))
fileObject = open('/Users/zq1/Downloads/sampleList.txt', 'w')
for idx in (rule+sh):
        fileObject.write(idx)
        fileObject.write('\n')
fileObject.close()
print(rule)
print(rule+sh)