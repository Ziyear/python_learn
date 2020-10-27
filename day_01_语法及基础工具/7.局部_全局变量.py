a = 100  # 全局变量


def test1():
    b = 200  # 局部变量


def test2():
    # 找不到 b
    # print("a=%d,b=%d" % (a, b))
    pass


test2()

name = "ziyear"


def get_name():
    # 这里的name只是局部变量
    # name = "ZIYEAR"

    # 声明 name为全局变量，那么这里修改就是修改全局变量
    global name
    name = "Ziyear"


def print_name():
    print("姓名是：%s" % name)


get_name()
print_name()
