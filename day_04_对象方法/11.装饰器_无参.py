

def no_cus(func):
    print("----no_cus-1-----")

    def no_cus_inner():
        print("----no_cus_inner-1------")
        func()
        print("----no_cus_inner-2------")

    print("----no_cus-2-----")
    return no_cus_inner


@no_cus
def test():
    print("---test---")


test()
