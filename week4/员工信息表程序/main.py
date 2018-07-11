#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/7/11 19:24
# software: PyCharm

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Colin Yao
"""python 员工信息表操作"""
import sys
import os


def select1():
    '''
    查看文件函数
    :return:
    '''
    with open('peopledb', 'r', encoding='utf-8') as f:
        line = f.readlines()
        for i in line:
            print(i)
def select():
    '''
    查询函数
    :return:
    '''
    msg = '''
    请输入或复制查询命令例如：

    　　  1. select name,age from staff_table where age > 22
　　      2. select * from staff_table where dept = "IT"
          3. select * from staff_table where enroll_date like "2013"
    '''
    print(msg)
    user_choice_input = input(">>>:")
    user_choice_input1 = user_choice_input.split(' ')
    if user_choice_input == 'select name,age from staff_table where age > %s' % (user_choice_input1[7]):
        with open('peopledb', 'r+', encoding='utf-8') as f:
            list1 = []
            count = 0
            for line in f:
                i = line.strip().split(',')
                if i[2] > user_choice_input1[7]:
                    list1.append(i)
            for s in list1:
                count = count + 1
            for j in list1:
                print(j)
            print('满足条件的个数为>>:%s' % (count))
    elif user_choice_input == ('select * from staff_table where dept = %s' % (user_choice_input1[7])):
        with open('peopledb', 'r+', encoding='utf-8') as f:
            list2 = []
            count = 0
            for line in f:
                i1 = line.strip().split(',')
                if i1[4] == eval(user_choice_input1[7]):
                    list2.append(i1)
            for s1 in list2:
                count = count + 1
                # print(list1)
            for j1 in list2:
                print(j1)
            print('满足条件的个数为>>:%s' % (count))
    elif user_choice_input == ('select * from staff_table where enroll_date like %s' % (user_choice_input1[7])):
        with open('peopledb', 'r+', encoding='utf-8') as f:
            list3 = []
            list4 = []
            count = 0
            for line in f:
                i = line.strip().split(',')
                list3.append(i)
            for j in list3:
                m = j[5].split('-')
                if m[0] == eval(user_choice_input1[7]):
                    list4.append(j)
            for s in list4:
                count = count + 1
                if count < 1:
                    print("没有找到类似的条目:")
                    pass
                else:
                    pass
            for j in list4:
                print(j)
            print('满足条件的条数为>>:%s' % (count))
    return ()


def alter():
    '''
    添加函数
    :return:
    '''
    msg = '''

    1)添加命令如下：Jack Wang,30,13304320533,HR,2015-05-03

    '''
    print(msg)
    user_choice_input = input("请输入命令>>>:")
    user_choice_input1 = user_choice_input.split(',')
    with open('peopledb', 'r+', encoding='utf-8') as f:
        list = []
        for line in f:
            s2 = line.strip().split(',')
            m = s2[3]
            list.append(m)
        if user_choice_input1[2] in list:
            print('这条记录已经存在')
            main()
        else:
            my_index = str(len(list) + 1)
            user_choice_input1.insert(0, my_index)
            user_choice_input1 = ','.join(user_choice_input1)
        f.write('\n')
        f.write(user_choice_input1)
        f.close()
        print("记录添加完成", '\n')
        select1()
    return ()


def delect():
    '''
    删除函数
    :return:
    '''
    print("请输入删除命令例如: 输入用户ID 既可以从staff_table里删除")
    msg = '''
        1)按1 删除、直接删除ID即可
        2)按2或者q退出
        3)按任意返回上一层
    '''
    print(msg)
    user_choice_input = input("请输入命令>>>: ")
    if user_choice_input == '1':
        print("现有的用户为:")
        select1()
        print('\n')
        user_choice_input1 = input("请输入需要删除的用户ID:")
        user_choice_input2 = user_choice_input1[0]
        f = open('peopledb', 'r+', encoding='utf-8')
        f1 = open('new_peopledb', 'w+', encoding='utf-8')
        for line in f:
            i = line.strip().split(',')
            i1 = i[0]
            if user_choice_input2 != i1:
                i = ','.join(i)
                f1.write(i)
                f1.write('\n')
            else:
                continue
        f.close()
        f1.close()
        os.remove('peopledb')
        os.rename('new_peopledb', 'peopledb')
        print('\n')
        select1()
    elif user_choice_input == '2' or 'q':
        sys.exit()
    return ()


def update():
    '''
    更新函数
    :return:
    '''
    msg = '''
    1)这里第一个等号按照没有空格的格式划分
    2)命令范例:UPDATE staff_table SET dept="INS" where dept = "HR"
    '''
    print(msg)
    user_choice_input = input("请输入命令>>>:")
    user_choice_input1 = user_choice_input.split(' ')
    dept = user_choice_input1[3].split('=')
    dept_new = dept[1]
    dept_old = user_choice_input1[7]
    if user_choice_input == ('UPDATE staff_table SET dept=%s where dept = %s' % (dept_new, dept_old)):
        dept_new1 = eval(dept_new)
        dept_old1 = eval(dept_old)
        f = open('peopledb', 'r+', encoding='utf-8')
        f1 = open('new_peopledb', 'w+', encoding='utf-8')
        for line in f:
            i = line.strip().split(',')
            dept_change = i[4]
            if dept_change == dept_old1:
                i[4] = eval(dept_new)
            i = ','.join(i)
            f1.write(i)
            f1.write('\n')
        f.close()
        f1.close()
        os.remove('peopledb')
        os.rename('new_peopledb', 'peopledb')
        print('\n')
        select1()
        pass
    return ()


def main():
    '''
    交互程序
    :return:
    '''
    print("员工信息表操作作业练习")
    msg = '''
        1）查询
        2）添加
        3）删除
        4）更新
        5) 退出
      '''
    exit_flag = False
    while not exit_flag:
        print(msg)
        user_choice = input("请选择>>:")
        if user_choice == '1':
            select()
        elif user_choice == '2':
            alter()
        elif user_choice == '3':
            delect()
        elif user_choice == '4':
            update()
        elif user_choice == '5' or 'q':
            sys.exit()
        else:
            print("您的选择有误、请重新输入")


main()