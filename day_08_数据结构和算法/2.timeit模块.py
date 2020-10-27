import timeit


def test1():
    li = []
    for i in range(10000):
        li.append(i)


def test2():
    li = []
    for i in range(10000):
        # li += [i]
        li = li + [i]


def test3():
    li = [i for i in range(10000)]


def test4():
    li = list(range(10000))


def test5():
    li = []
    for i in range(10000):
        li.extend([i])


def test6():
    li = []
    for i in range(10000):
        li.insert(0, i)


timer = timeit.Timer("test1()", "from __main__ import test1")
print("append                    花费：" + str(timer.timeit(number=1000)))
timer = timeit.Timer("test2()", "from __main__ import test2")
print("+=                        花费：" + str(timer.timeit(number=1000)))
timer = timeit.Timer("test3()", "from __main__ import test3")
print("[i for i in range(10000)] 花费：" + str(timer.timeit(number=1000)))
timer = timeit.Timer("test4()", "from __main__ import test4")
print("list(range(10000))        花费：" + str(timer.timeit(number=1000)))
timer = timeit.Timer("test5()", "from __main__ import test5")
print("extend                    花费：" + str(timer.timeit(number=1000)))
timer = timeit.Timer("test6()", "from __main__ import test6")
print("insert                    花费：" + str(timer.timeit(number=1000)))
