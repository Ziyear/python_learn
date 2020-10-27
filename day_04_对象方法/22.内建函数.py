print("######## range ########")
a = range(5)
print(list(a))
a = [x + 2 for x in range(5)]
print(list(a))

print("######## map ########")
b = map(lambda x: x * x, [1, 2, 3])
print(list(b))
b = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print(list(b))


def f1(x, y):
    return (x, y)


l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
l3 = map(f1, l1, l2)
print(list(l3))

print("######## filter ########")

f = filter(lambda x: x % 2, [1, 2, 3, 4])
print(list(f))

print("######## reduce ########")
from functools import reduce

r = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(r)
r = reduce(lambda x, y: x + y, [1, 2, 3, 4], 5)
print(r)
r = reduce(lambda x, y: x + y, ['aa', 'bb', 'cc'], 'dd')
print(r)

print("######## sorted ########")

print(sorted([2, 1, 3, 5, 6, 4]))
print(sorted([2, 1, 3, 5, 6, 4], reverse=True))
print(sorted(['dd', 'aa', 'bb', 'cc']))
print(sorted(['dd', 'aa', 'bb', 'cc'], reverse=True))
