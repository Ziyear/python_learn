def func_arg(arg):
    def common_wrapper(func):
        def has_cus_inner(*args, **kwargs):
            print("----记录日志- arg：%s----" % arg)
            if arg == "aaa":
                func(*args, **kwargs)
                func(*args, **kwargs)
            else:
                func(*args, **kwargs)
        return has_cus_inner

    return common_wrapper


@func_arg("aaa")
def test1():
    print("--- test1 ---")


@func_arg("bbb")
def test2():
    print("--- test2 ---")


test1()
test2()
