class Test(object):
    def __init__(self, switch):
        self.switch = switch

    def calc(self, a, b):
        try:
            return a / b
        except Exception as result:
            if self.switch:
                print("捕捉异常开启，已捕获到异常，信息如下：")
                print(result)
            else:
                # 重新抛出这个异常
                raise


a = Test(True)
a.calc(1, 0)

print("---------------------------")

a.switch = False
a.calc(1, 0)
