#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/4/9 13:47
# software: PyCharm




def shoppingcart(username,salary):
    ' 购物车主体函数 '

#    salary = input("请输入工资:")

    product_list = [
        ('Iphone',5800),
        ('mac',9800),
        ('bike',800),
        ('watch',5800),
        ('coffee',31),
        ('alex',100)
    ]

    shopping_list = []

    if salary.isdigit() :
        salary = int(salary)
        while True:
            for item in product_list:
                print(product_list.index(item),item)
            user_choice = input("选择要买吗>>>:")
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice < len(product_list) and user_choice >= 0:
                    p_item = product_list[user_choice]
                    if p_item[1] <= salary:
                        shopping_list.append(p_item)
#                        print(shopping_list, "\033[36;1放入购物车成功!\033[0m")
                        salary -=p_item[1]
                        print("\033[36;1m added %s into shopping cart ,your current balance is %s \033[0m" %(p_item,salary))
                    else:
                        print("\033[41;1m你的余额只剩[%s]\033[0m" %salary)
                else:
                    print("product code [%s] is not exist!" %user_choice)
            elif user_choice == 'q':
                print('------shoping list------')
                for p in shopping_list:
                    with open('./' + username + "/recording.txt", "a+", encoding="utf-8") as f:
                        p = str(p)
                        f.write(p+'\n')
                    print(p)
                with open('./' + username + "/salary.txt", "w+", encoding="utf-8") as f:
                    salary = str(salary)
                    f.write(salary)
                print("your current balance:", salary)
                exit()
            else:
                print("invalid option")

def Query_the_records(choose,username):

    if choose == 'y':
        with open('./' + username + "/recording.txt", "r", encoding="utf-8") as f:
            recording = f.read()  # 显示文本内容
            print(recording)
    else:
        pass