# 导入包
from pymysql import *

conn = None
cursor = None
try:
    # 获取连接
    conn = connect(host="ali.ziyear.com", port=3306, user="root", password="ZIYEAR@123456", db="python_test_01",
                   charset="utf8")
    # 获取执行器
    cursor = conn.cursor()
    sql = 'delete from t_student where id = 3'
    # 执行语句
    cursor.execute(sql)
    # 提交
    conn.commit()
    print("执行成功！")
except Exception as e:
    print("OS error: {0}".format(e))
finally:
    # 释放连接
    cursor.close()
    conn.close()
