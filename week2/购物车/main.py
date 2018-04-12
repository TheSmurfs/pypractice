#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/4/11 19:32
# software: PyCharm

import shoppingcart


def main():
    with open("user.txt","r",encoding="utf-8") as f:#获取user.txt内容
        user_info = f.read() # 显示文本内容
        #print(user_info)
        user_list = user_info.split() # 加入列表
        #print(user_list)
        user_dic = {} # 定义空字典
        for itme in user_list: # 循环user_list列表
            user_list = itme.split("-") # 截取-
            #print(user_list)
            user_dic[user_list[0]] = user_list[1] # 把文本中的内容截取----后加入字典
            #print(user_dic)
    count = 0 # count从0开始
    while count < 3:
        username = input("\033[38;1m请输入用户名-->>\033[0m:")
        if username in user_dic: #判断username是否在字典中
            #r+为读写模式
            with open("lock.txt", "r+", encoding="utf-8") as f:
                lock_info = f.read()
                lock_list = lock_info.split() #截取文本中的空格
                if username in lock_list:  # 判断输入的用户是否在被锁定文件中
                    print("\033[31;1m此用户被锁定,请联系管理员解绑\033[0m")
                else:
                    password = input("\033[38;1m请输入密码-->>\033[0m:")
                    #print(user_dic)
                    if password == user_dic[username]:#判断字典中帐号密码是否正确

                        print("%s:\033[36;1m登录成功!\033[0m"%username)
                        shoppingcart.shoppingcart()
                        exit()
                    else:
                        count +=1 #密码每次错误数量加1
                        if count==3: #错误3次帐号锁定
                            f.write('\n'+username)
                            print("\033[31;1m密码错误3次，帐号已被锁定\033[0m")
                        else:
                            print("\033[31;1m密码错误，还可以再试%s次\033[0m"%(3-count))
        else:
            print("\033[31;1m用户名输入错误！\033[0m")

if __name__ == '__main__':
    main()
