a = [i for i in range(1, 18)]
print(a)

b = [10 for i in range(1, 10)]
print(b)

c = [i for i in range(10) if i % 2 == 0]
print(c)

d = [i for i in range(3) for j in range(2)]
print(d)

e = [(i, j) for i in range(3) for j in range(2)]
print(e)
