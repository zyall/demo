l=[2870,2874,2872,2871,2871,2872]
s=[]
x=int(input("请输入："))  #输入数字
x1=min(l)
y1=max(l)
for i in l:
    s.append(x-i)
print("最大误差:",max(s))    #最大误差
print("极差:",abs(x1-y1))  #极差