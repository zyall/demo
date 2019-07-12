#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print(R,end='\n')
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])
'''5

rows=int(input("输入列数："))
i=j=k=1
print("等腰三角形：")

for i in range(0,rows):
    for k in range(0,rows-i):
        print("*",end='')

    print("\n")


print("hello,liaoyujie")