#!/usr/bin/python
# -*- coding:utf-8 -*-
import json


f = open("test.json", 'w')
dic = {}
for i in range(1, 10):
    if i % 2 == 0:
        new_context = "C++" +'\n'
        f.write(new_context)
    else:
        new_context = "python" +'\n'
        f.write(new_context)

    # jsObj = json.dumps(dic)  # 将dict格式的转成str写入json格式的文件
    #
    # fileObject.write(jsObj)
    # fileObject.write('\n')
f.close()
