import hashlib
from mymysql.MysqlHelper import MysqlHelper
from myredis.RedisHelper import RedisHelper


def md5(str):
    md5 = hashlib.md5(str.encode())
    return md5.hexdigest()


def login(username, password):
    pwd_md5 = md5(password)
    redis_helper = RedisHelper(host="ali.ziyear.com", port=6379, password="ZIYEAR@123456")
    value = redis_helper.get(username)
    value = str(value, encoding="utf-8")
    if value == pwd_md5:
        print("redis登录成功")
    else:
        mysql_helper = MysqlHelper(host="ali.ziyear.com", port=3306, user="root", password="ZIYEAR@123456",
                                   db="python_test_01",
                                   charset="utf8")
        sql = "select * from t_user where username=%s and is_deleted = 'n'"
        result = mysql_helper.execute(sql, [username])
        if result:
            for user in result:
                if user.get("password") == pwd_md5:
                    print("mysql登录成功")
                    redis_helper.set(username, pwd_md5)
                else:
                    print("用户名或密码错误！")
        else:
            print("用户名或密码错误！")


if __name__ == '__main__':
    username = input("请输入用户名   ：")
    password = input("请输入密码     ：")
    login(username, password)
