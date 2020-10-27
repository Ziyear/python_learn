a = 4
b = 5

# 1
c = 0
c = a
a = b
b = c
print("a = %d,b = %d" % (a, b))
# 2
a = 4
b = 5
a = a + b
b = a - b
a = a - b
print("a = %d,b = %d" % (a, b))
# 3
a = 4
b = 5
a, b = b, a

print("a = %d,b = %d" % (a, b))


def test(num):
    num += num
    print(num)


test(100)  # 200
test([100])  # [100, 100]
