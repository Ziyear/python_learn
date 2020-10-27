# __getattribute__ 属性访问拦截器
class Person():
    def __init__(self, subject):
        self.subject = subject
        self.jack = "cpp"

    def __getattribute__(self, item):
        if item == 'subject':
            print("log subject")
            return 'redirect python'
        # else: # 注释掉这两行，将找不到属性jack
        #     return object.__getattribute__(self, item)


p = Person("python")
print(p.subject)
print(p.jack)

print("####################")


class ItPark():
    def __getattribute__(self, item):
        if item.startswith("a"):
            return 'haha'
        else:
            return self.test

    def test(self):
        print("haha")


t = ItPark()
print(t.a)
print(t.b)  # maximum recursion depth exceeded while calling a Python object 调用Python对象时超出了最大递归深度
