class Dog(object):
    def __init__(self):
        print("------__init__ method------")

    def __del__(self):
        print("------__del__ method------")

    def __str__(self):
        print("------__str__ method------")
        return "对象的描述。"

    def __new__(cls):  # cls 指向Dog指向的那个类对象
        print(id(cls))
        print("------__new__ method------")
        return object.__new__(cls)


print(id(Dog))

# 相当于做了3件事情
# 1.调用new方法来创建对象，然后找了一个对象接受返回值，返回值表示创建出来的对象的引用
# 2.调用init方法，传递进去一个刚刚创建的一个对象的引用
# 3.返回对象的引用
dog = Dog()  # ------__new__ method------
