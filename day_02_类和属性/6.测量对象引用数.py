import sys


class T:
    pass


t = T()
t1 = t
getrefcount = sys.getrefcount(t) # 获取到的引用个数是实际引用个数+1


print(getrefcount)
