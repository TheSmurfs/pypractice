#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/4/12 21:45
# software: PyCharm
import shoppingcart

def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
#    path = path.strip()
    # 去除尾部 \ 符号
#    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path + ' 用户第一次登陆')
        # 创建目录操作函数
        os.makedirs(path)
        with open('./' + 'fcq' + "/recording.txt", "w+", encoding="utf-8") as f:
#            p = str(p)
            f.write('666666' + '\n')
        shoppingcart.shoppingcart()
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 用户已登陆过')

        shoppingcart.shoppingcart()
        return False


# 定义要创建的目录
mkpath = "fcq"
# 调用函数
mkdir(mkpath)