class Dog:
    def __init__(self, name):
        self.name = name
        self.__age = 0  # 定义了一个私有属性

    def set_age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age

    def __test(self):
        print("私有方法")

    def def_test(self):
        self.__test()


dog = Dog("大黄")
dog.set_age(18)
age = dog.get_age()
print(age)

dog.def_test()