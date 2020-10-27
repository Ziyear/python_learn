def has_cus(func):
    print("----has_cus-1-----")

    def has_cus_inner(*args, **kwargs):
        print("----has_cus_inner-1------")
        value = func(*args, **kwargs)
        print("----has_cus_inner-2------")
        return value + " proxy"

    print("----has_cus-2-----")
    return has_cus_inner


@has_cus
def test(a, b, c):
    print("--- test1:a:%d, b:%d, c:%d---" % (a, b, c))
    return "test1"


test_ = test(11, 22, 33)

print("test return val : %s" % test_)
