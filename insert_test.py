#insert_test.py
#pymysql 查询示例
#导入pymysql模块

import pymysql
from db_conf import *
#连接数据库
conn = pymysql.connect(
    host,user,passwd,dbname)
#获取游标
cursor = conn.cursor()
#执行sql
# sql = """insert into orders(order_id,cust_id)
# values('201801010007','c00000007')
# """ #添加

sql = "delete from orders where order_id='201801010007'" #删除

cursor.execute(sql) #执行插入
conn.commit()  #提交事务
print("执行成功")
cursor.close()    #关闭游标
conn.close()      #关闭数据库连接
