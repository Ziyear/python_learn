class Test(object):
    def __init__(self):
        self.__num = 100
        self.__money = 0

    def setNum(self, num):
        print("----setNum----")
        self.__num = num

    def getNum(self):
        print("----getNum----")
        return self.__num

    num = property(getNum, setNum)

    @property
    def money(self):
        print("----get money----")
        return self.__money

    @money.setter
    def money(self, money):
        print("----set money----")
        self.__money = money


t = Test()

t.num = 1000
print(t.num)

t.money = 19
print(t.money)
