#coding=utf-8
'''
import re
a = ["开wifi", "关wifi", "电量30", "电量40", "电量50"] # a可以取值的列表
b = ["使用QQ", "打电话", "使用浏览器", "使用文本", "使用计算器"]  # b可以取值的列表
rule=['电量30-使用QQ', '电量40-打电话', '开wifi-使用QQ',"电量30-打电话"] #约束规则
comb=[] #脚本结果
for i in rule:
    condition,result.txt=i.split("-")
    for x in range(len(a)):
        for j in a:
            if j in condition:
                a.remove(j)
comb = [m + n for m in a for n in b]
rule=rule.replace('-','')
for k in rule:
    comb.append(k)
print(comb)
print(len(comb))
fileObject = open('/Users/zq1/Downloads/sampleList.txt', 'w')
for idx in comb:
        fileObject.write(idx)
        fileObject.write('\n')
fileObject.close()
'''
import re

a = ["123", "456", "789"]
d = {"B": "2", "E": "5", "H": "8"}
b = ",".join(a)
print(b)

for i in d.keys():
    b = re.sub(d[i], i, b)
print(b.split(","