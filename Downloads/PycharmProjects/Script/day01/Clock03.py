#!/usr/bin/python
#ecoding:utf-8


m=int(input("请输入："))
for i in range(1,85):
    if m % i==0:
        j=m / i;
        if i>j and (i+j)%2==0 and (i-j)%2==0:
            m=(i+j)/2
            n=(i-j)/2
            x=n*n-100
            print(x)