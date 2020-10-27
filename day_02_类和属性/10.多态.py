class Dog(object):
    def print_self(self):
        print("大家好，我是xxx，希望大家以后多多关照！")
class XiaoTian(Dog):
    def print_self(self):
        print("hello everybody, 我是你们的老大，我是xxx")

def introduce(temp):
    temp.print_self()

dog1 = Dog()
dog2 = XiaoTian()

introduce(dog1)
introduce(dog2)