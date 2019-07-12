''''
result=[]
fo=open("/Users/zq1/Downloads/sampleList.txt","r")
line=fo.readline()
for line in fo:
    result.append(line.split(","))
print(result)
'''
result=[]
fo=open("/Users/zq1/Downloads/sampleList.txt","r+")
#line=fo.readlines()
for line in fo.readlines():
    line=line.strip('\n')
    result.append(line)
