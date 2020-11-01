from mysql.MysqlHelper import MysqlHelper


def insert(helper):
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    address = input("请输入学生地址：")
    sql = 'insert into t_student(name,age,address) values (%s, %s, %s)'
    helper.update(sql, [name, age, address])


def select(helper):
    sql = 'select * from t_student where id <5'
    result = helper.execute(sql)
    print(result)


if __name__ == '__main__':
    helper = MysqlHelper(host="ali.ziyear.com", port=3306, user="root", password="ZIYEAR@123456", db="python_test_01",
                         charset="utf8")
    select(helper)
