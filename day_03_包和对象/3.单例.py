class Dog(object):
    __instance = None
    __init_flag = False

    def __init__(self, name):
        if Dog.__init_flag == False:
            self.name = name
            Dog.__init_flag = True

    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


dog1 = Dog("旺财")
print(dog1.name)
print(id(dog1))

dog2 = Dog("哮天犬")

print(id(dog2))
print(dog2.name)
print("--------------------------")
print(dog1.name)
