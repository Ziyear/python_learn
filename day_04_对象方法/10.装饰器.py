def foo():
    print("foo")


foo()

foo = lambda x: x + 1
print(foo(1))

print("################################")


# 装饰方法
def w1(func):
    def inner():
        print("---正在验证权限---")
        func()

    return inner


# 对f1进行装饰 == f1 = w1(f1)
@w1
def f1():
    print("----f1----")


f1()
print("################################")


# 定义函数，完成数据包裹
def makeBold(func):
    def wrapped():
        return "<b>" + func() + "</b>"

    return wrapped


def makeItalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"

    return wrapped


# 谁在下边先执行谁
@makeBold
@makeItalic
def test1():
    return "Hello test1"


print(test1())
