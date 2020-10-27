class Dog:
    def __del__(self):
        print("======Dog del ======")


dog1 = Dog()

dog2 = dog1

del dog1  # 删除指向
del dog2  # 删除指向
# 对象没有引用的时候自动回收
print("===========")
