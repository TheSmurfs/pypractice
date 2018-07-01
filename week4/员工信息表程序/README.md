员工信息表程序
---
#### 要求
员工信息表程序，实现增删改查操作：



可进行模糊查询，语法至少支持下面3种:

　　select name,age from staff_table where age > 22

　　select  * from staff_table where dept = "IT"

select  * from staff_table where enroll_date like "2013"

查到的信息，打印后，最后面还要显示查到的条数

可创建新员工纪录，以phone做唯一键，staff_id需自增

可删除指定员工信息纪录，输入员工id，即可删除

可修改员工信息，语法如下:

　　UPDATE staff_table SET dept="Market" where dept = "IT"

注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码

#### 流程

![image](https://github.com/TheSmurfs/Githubphotos/blob/master/%E6%B5%81%E7%A8%8B%E5%9B%BE/%E6%A8%A1%E6%8B%9F%E7%99%BB%E9%99%86.png?raw=true)