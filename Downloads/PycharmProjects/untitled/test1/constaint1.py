a=['1','2','3','4'] # a可以取值的列表
b=['a','b','c','d']# b可以取值的列表
condtion=['1','2']
rule=['1a','2a']

for x in range(len(a)):
    for i in a:
        if i in condtion:
            a.remove(i)
l = [m + n for m in a for n in b]
for j in rule:
    l.append(j)
print(l)


