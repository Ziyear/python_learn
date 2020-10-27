# 导入包
from pymysql import *

conn = None
cursor = None
try:
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    address = input("请输入学生地址：")
    # 获取连接
    conn = Connect(host="123.57.44.168", port=3306, user="root", password="ZIYEAR@123456", db="python_test_01",
                   charset="utf8")
    # 获取执行器
    cursor = conn.cursor()

    sql = 'insert into t_student(name,age,address) values (%s, %s, %s)'
    # 执行语句
    cursor.execute(sql, [name, age, address])
    # 提交
    conn.commit()
    print("执行成功！")
except Exception as e:
    print("OS error: {0}".format(e))
finally:
    # 释放连接
    cursor.close()
    conn.close()
