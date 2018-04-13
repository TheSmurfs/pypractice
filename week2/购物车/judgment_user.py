#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/4/12 21:45
# software: PyCharm
import shoppingcart

def mkdir(path):
    '判断是否是第一次登录'
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
        salary = input("请输入工资:")
        # 创建目录操作函数
        os.makedirs(path)
        shoppingcart.shoppingcart(path, salary)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 用户已登陆过')
        choose = input("\033[36;1m 是否查询之前消费记录(查询请输入y，不查询任意键)-->> \033[0m:")
        shoppingcart.Query_the_records(choose, path)
        with open('./' + path + "/salary.txt", "r+", encoding="utf-8") as f:
            salary = f.read()
        print("余额剩余：", salary)
        shoppingcart.shoppingcart(path, salary)
        return False
