#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/4/3 20:20
# software: PyCharm

with open("menu.txt","r",encoding="utf-8") as f:
    f_str = f.read()     #将文件内容转换为字符串
    #print(f_str)
    file_str = str(f_str)  # 将每行信息转成字符串格式
    type(file_str)
    #menu = eval(f.readline())    #将字符串转换为字典
    menu = eval(file_str.strip())
exit_flag = False
while not exit_flag:
    for i in menu:
        print(i)

    choice = input("请选择省份直辖市:")
    if choice in menu:
        while not exit_flag:
            for i2 in menu[choice]:
                print(i2)
            choice2 = input("请选择镇区>>>")
            if choice2 in menu[choice]:
                while not exit_flag:
                    for i3 in menu[choice][choice2]:
                        print(i3)
                    choice3 = input("请选择小地名>>>")
                    if choice3 in menu[choice][choice2]:
                        for i4 in menu[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input("最后一层>>>按b退出")
                        if choice4== "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                 break
            elif choice2 == "q":
                exit_flag = True