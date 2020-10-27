# 可以用于for循环的对象，统称为可迭代对象
# list，tuple，dict，set，str 等
from collections.abc import Iterable
from collections.abc import Iterator

# 判断是可迭代对象
print(isinstance(100, Iterable))
print(isinstance("abc", Iterable))
# 判断迭代器
print(isinstance([], Iterator))

# 转换迭代器
i = iter("abc")
print(next(i))
print(next(i))
print(next(i))
