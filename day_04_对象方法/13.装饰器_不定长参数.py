
def has_cus(func):
    print("----has_cus-1-----")

    def has_cus_inner(*args, **kwargs):
        print("----has_cus_inner-1------")
        func(*args, **kwargs)
        print("----has_cus_inner-2------")

    print("----has_cus-2-----")
    return has_cus_inner


@has_cus
def test1(a, b, c):
    print("--- test1:a:%d, b:%d, c:%d---" % (a, b, c))


@has_cus
def test2(a, b, c, d):
    print("--- test2:a:%d, b:%d, c:%d, d:%d---" % (a, b, c, d))


test1(11, 22, 33)
test2(11, 22, 33, 44)
