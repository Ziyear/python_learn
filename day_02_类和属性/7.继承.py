class Animal:
    def eat(self):
        print("===== 吃 =====")

    def drink(self):
        print("===== 喝 =====")

    def sleep(self):
        print("===== 睡 =====")

    def run(self):
        print("===== 跑 =====")


class Dog(Animal):  # 继承 在类后边加个括号 括号里面放上父类
    def bark(self):
        print("===== 汪汪叫 =====")


class XiaoTianQuan(Dog):
    # 重写父类方法
    def bark(self):
        # Dog.bark(self)  # 调用父类的方法 1
        super().bark()  # 调用父类的方法 2
        print("===== 升级为狂叫 =====")

    def fly(self):
        print("===== 飞起来了卧槽 =====")


class Cat(Animal):  # 继承 在类后边加个括号 括号里面放上父类
    def catch(self):
        print("===== 抓老鼠 =====")


print("=======================")
wangcai = Dog()
wangcai.eat()
wangcai.bark()
print("=======================")
xtq = XiaoTianQuan()
xtq.eat()
xtq.bark()
xtq.fly()
print("=======================")
cat = Cat()
cat.run()
cat.catch()
