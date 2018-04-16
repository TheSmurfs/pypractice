#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/4/13 21:49
# software: PyCharm


def select():
    '查询员工工资'
    with open("info.txt", "r", encoding="utf-8") as f:
        fsb = f.readlines()
#        print(fsb)
    user_choice = input("请输入你要查询的员工姓名：")
    for line in fsb:
#        print(line)
        print(user_choice.split())
        print(line.split())
        if user_choice.split()[0] in line.split()[0]:
            print(user_choice, "的工资是：",line.split()[1])

def update():
    '修改员工工资'
    with open("info.txt", "r", encoding="utf-8") as f:
        fsb = f.readlines()
    user_choice_1 = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：").strip()
    with open("info.txt", "w", encoding="utf-8") as f1:
        for user_list in fsb:
            if user_choice_1.split()[0] in user_list.split()[0]: #判断输入的员工是否在文本中
                user_list = user_list.replace(user_list.split()[1], user_choice_1.split()[1]) # 修改员工工资
            f1.write(user_list)
    print("修改成功")

def add():
    '添加新员工'
    user_add = input("请输入要增加的员工姓名和工资（例如：Eric 100000）：")
    with open("info.txt", "a", encoding="utf-8") as f:
        f.write('\n' + user_add)
        print("添加成功")

def delete():
    '删除员工'
    with open("info.txt", "r+", encoding="utf-8") as f:
        fsb = f.readlines()
    user_choice = input("请输入要删除的员工姓名：").strip()
    with open("info.txt", "w+", encoding="utf-8") as f1:
        for user_list in fsb:
            print(user_choice)
            print(user_list.split()[0])
            if user_choice in user_list.split()[0]:  # 判断输入的员工是否在文本中
#                print(user_list.split()[0])
#                print(user_list.split()[1])
#                user_list.split().remove(user_list.split()[0]) # 删除姓名
#                user_list.split().remove(user_list.split()[1]) # 删除工资
                print("删除成功")
                continue
            print(user_list)
            f1.write(user_list)

while True:
    user_chioce = '''
    1.查询员工工资
    2.修改员工工资
    3.增加新员工记录
    4.删除员工
    5.退出
    '''
    print(user_chioce)
    user_choice = input("请输入你的选择:")
    if user_choice.isdigit(): # 判断输入的是否数字类型
        if user_choice == '1':
            select() # 查询
        elif user_choice == '2':
            update() # 修改
        elif user_choice == '3':
            add() # 添加
        elif user_choice == '4':
            delete() # 删除
        elif user_choice == '5':
            exit() # 退出
        else:
            print("请输入正确的选项")
    else:
        print("请输入正确的选项")