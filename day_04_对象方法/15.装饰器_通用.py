def common_wrapper(func):
    def has_cus_inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret

    return has_cus_inner


@common_wrapper
def test1():
    print("--- test1---")


@common_wrapper
def test2(a, b, c):
    print("--- test1:a:%d, b:%d, c:%d---" % (a, b, c))


@common_wrapper
def test3():
    return "test3"


@common_wrapper
def test4(a, b):
    return "test4 a:%d, b:%d" % (a, b)


test1()
test2(11, 22, 33)
test3ret = test3()
test4ret = test4(11, 22)
print("test3 return val : %s" % test3ret)
print("test4 return val : %s" % test4ret)