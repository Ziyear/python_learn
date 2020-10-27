class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test(self):
        print("===== test ====")

    def __test(self):
        print("==== private test ====")

    def test2(self):
        self.__test()
        print(self.__num2)
        print("===== test2 ====")


class B(A):
    pass

    def test3(self):
        # self.__test() #不能调用父类的私有方法
        # print(self.__num2) #不能调用父类的私有属性
        print("===== test3 ====")


b = B()
b.test()
# b.__test()  # 私有方法不能被继承
print(b.num1)
# print(b.__num2) # 私有属性不能被继承
b.test2()
b.test3()
