#query_test.py
#pymysql 查询示例
#导入pymysql模块

import pymysql
from db_conf import *
# #建立数据连接
# host = "localhost" #服务器地址127.0.0.1
# user = "root"    #连接数据库的用户名
# passwd="123456"    #密码
# dbname = "eshop"     #连接哪一个库

#调用pymysql模块下的connect函数连接数据库
#连接成功后，返回一个连接对象，放到conn变量中
conn = pymysql.connect(
    host, user ,passwd ,dbname)

cursor = conn.cursor()#创建游标对象

#使用游标对象提供的方法，执行sql语句
sql = "select * from orders"
cursor.execute(sql)  #执行sql语句
result = cursor.fetchall() #取出所有的数据
for row in result:  #循环取出每行的数据并打印
    order_id =row[0]  #订单编号
    cust_id = row[1]    #客户编号
    amt = row[5]    #金额
    print("编号：%s,编号：%s,金额：%s"%
    (order_id,cust_id,amt))

#提交事务（如果需要）
#关闭游标
cursor.close()
#关闭数据库
conn.close()



