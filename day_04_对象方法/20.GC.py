import gc


class classA():
    def __init__(self):
        print("object born, id:%s" % (hex(id(self))))


def f3():
    print("----0----")
    # print(gc.collect())
    c1 = classA()
    c2 = classA()
    c1.t = c2
    c2.t = c1
    print("----1----")
    del c1
    del c2
    print("----2----")
    print(gc.garbage)
    print("----3----")
    print(gc.collect())  # 显示回收
    print("----4----")
    print(gc.garbage)
    print("----5----")
    print(gc.get_threshold())


if __name__ == '__main__':
    gc.set_debug(gc.DEBUG_LEAK)  # 设置gc模块日志
    f3()
