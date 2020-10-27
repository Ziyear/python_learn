def test():
    print("---test---")


test()

# 输出test() 指向的函数体
print(test)

b = test

b()

print("######################################")


def num(number):
    print("---1---")

    def num_in(num_in):
        print("---2---")
        print(number + num_in)

    print("---3---")
    return num_in


ret = num(100)
print(ret)
ret(2)
ret(3)
print("######################################")


# 应用 计算 a*x+b
def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5))
print(line2(5))
