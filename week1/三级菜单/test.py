#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/4/5 22:49
# software: PyCharm

with open("menu.txt","r",encoding="utf-8") as f:
    f_str = f.read()     #将文件内容转换为字符串
    print(f_str)
    file_str = str(f_str)  # 将每行信息转成字符串格式
    type(file_str)
    #menu = eval(f.readline())    #将字符串转换为字典
    #menu = eval(file_str)