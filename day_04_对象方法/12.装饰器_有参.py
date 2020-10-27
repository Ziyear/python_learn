

def has_cus(func):
    print("----has_cus-1-----")

    def has_cus_inner(a, b):
        print("----has_cus_inner-1------")
        func(a, b)
        print("----has_cus_inner-2------")

    print("----has_cus-2-----")
    return has_cus_inner


@has_cus
def test(a, b):
    print("--- test:a:%d, b:%d ---" % (a, b))


test(11, 22)
