def test1(a, b):
    return a + b


result = test1(1, 2)

# 匿名函数
test2 = lambda a, b: a + b

result2 = test2(11, 22)

print("result=%d,result2=%d" % (result, result2))
print("=" * 100)
infors = [{"name": "zhangsan", "age": 10}, {"name": "lisi", "age": 13}, {"name": "wangwu", "age": 11}]

infors.sort(key=lambda x: x["age"])
print(infors)
print("=" * 100)


def test_fun(a, b, func):
    result = func(a, b)
    return result


num = test_fun(111, 222, lambda x, y: x + y)
print(num)

print("=" * 100)


def test_input_func(a, b, func):
    result = func(a, b)
    return result


func_new = input("请输入一个匿名函数：")
func_new = eval(func_new)

num = test_input_func(1111, 2222, func_new)
print(num)
