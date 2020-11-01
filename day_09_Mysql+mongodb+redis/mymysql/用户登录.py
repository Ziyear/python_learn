import hashlib
from mymysql.MysqlHelper import *

def md5(str):
    md5 = hashlib.md5(str.encode())
    return md5.hexdigest()


def login(username, password):
    helper = MysqlHelper(host="ali.ziyear.com", port=3306, user="root", password="ZIYEAR@123456", db="python_test_01",
                         charset="utf8")
    sql = "select * from t_user where username=%s and is_deleted = 'n'"
    result = helper.execute(sql, [username])
    if result:
        for user in result:
            pwd_md5 = md5(password)
            if user.get("password") == pwd_md5:
                print("登录成功")
            else:
                print("用户名或密码错误！")
    else:
        print("用户名或密码错误！")


if __name__ == '__main__':
    username = input("请输入用户名   ：")
    password = input("请输入密码     ：")
    login(username, password)
