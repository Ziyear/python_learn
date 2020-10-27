class Test(object):
    def __init__(self):
        self.__num = 100

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num


"""
xx      : 公有变量
_x      : 单前置下划线 私有化属性方法，from xx import * 禁止导入 类对象和子类可以访问
__xx    : 双前置下划线 避免与子类中属性名冲突，无法在外部直接访问（名字重整所以访问不了）
__xx__  : 前后双下划线，用户命名空间魔法对象或属性，例如 __init__, 不要自己定义这种样式
xx_     : 后置单下划线，用于避免与python关键字冲突，没啥意义
"""

t = Test()
t.__num = 101110
print(t.getNum())
