a = [x * 2 for x in range(10)]
print(a)

# 创建生成器
b = (x * 2 for x in range(10))
print(b)  # <generator object <genexpr> at 0x02B42728>
for num in b:
    print(num)


# 斐波那契额数列
def createNum():
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a + b


a = createNum()
print(a)  # <generator object createNum at 0x0126CFB0>
for num in a:
    print(num)
