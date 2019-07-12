#!/usr/bin/python
# -*- coding: UTF-8 -*-


x=int(input("请输入："))
for  i in range(1,x):
    for j in range(1,x):
        if i==j*j:
            print(i,j)
