class Cat:
    # 属性

    # init
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # str
    def __str__(self):
        return "%s 的年龄是 %d" % (self.name, self.age)

    # 方法
    def eat(self):
        print("猫正在吃鱼。。。。")

    def drink(self):
        print("猫正在喝可乐。。。。")

    def introduce(self):
        print("%s 的年龄是 %d" % (self.name, self.age))


# 创建一个对象
cat = Cat("汤姆", 18)
cat.drink()
cat.eat()

# 添加属性
# cat.name = "汤姆"
# cat.age = 18

# 获取对象属性 1
# print("%s 的年龄是 %d" % (cat.name, cat.age))

# 获取对象属性 2
# cat.introduce()
print(cat)

lanmao = Cat("蓝猫", 20)
# lanmao.name = "蓝猫"
# lanmao.age = 20
# lanmao.introduce()
print(lanmao)
