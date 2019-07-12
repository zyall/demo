a=['A1','A2']
b=['B1','B2']
c=['C1','C2','C3']
d=['D1','D2']
e=['E1','E2']

#l=[a1 + b1 + c1 + d1 + e1 for a1 in a for b1 in b for c1 in c for d1 in d for e1 in e]

l=[a1 + c1 for a1 in a for c1 in c]

comb=[l1 + b1 for l1 in l for b1 in b]



print(comb)
fileObject = open('/Users/zq1/Downloads/sampleList.txt', 'w')
for idx in (comb):
        fileObject.write(idx)
        fileObject.write('\n')



