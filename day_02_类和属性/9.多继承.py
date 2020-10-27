class Base:
    def test(self):
        print("----- base.test -----")

    def xiangtong(self):
        print("----- base.xiangtong -----")


class A(Base):
    def test1(self):
        print("----- A.test1 -----")

    def xiangtong(self):
        print("----- A.xiangtong -----")


class B(Base):
    def test2(self):
        print("----- B.test2 -----")

    def xiangtong(self):
        print("----- B.xiangtong -----")


class C(A, B):
    def xiangtong(self):
        print("----- C.xiangtong -----")

    pass


c = C()
c.test()
c.test1()
c.test2()
# 获取方法调用查找链
print(C.__mro__)
c.xiangtong()
