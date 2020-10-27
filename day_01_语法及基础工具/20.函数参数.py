# 缺省参数
def test(a, b, c=1, d=0):
    print(a)
    print(b)
    print(c)
    print(d)


# test(a=1, b=2, c=3, d=100)
# test(1,2) == test(a=1, b=2)
test(a=1, b=2)


# 不定长参数 1
def test2(a, b, *args):
    print("=" * 50)
    print(a)
    print(b)
    print(args)

    result = a + b
    for num in args:
        result += num
    print("result=%d" % result)


# test2(1, 2, 3, 4, 4, 5, 6, 7, 8, 9)
test2(1, 2, 3)
test2(1, 2)


# test2(1) # 报错


# 不定长参数 2
def test3(a, b, c=3, *args, **kwargs):
    print("=" * 50)
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


a = (4, 5, 6)
kw = {"name": "ziyear", "age": 18}
test3(1, 2, 3, *a, **kw)  # * ** 表示对元祖和字典进行拆包
