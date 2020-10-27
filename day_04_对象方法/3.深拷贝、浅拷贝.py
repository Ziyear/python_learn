import copy

a = [11, 22, 33]
b = a

print("---------浅拷贝----------")
print("a:%s" % str(id(a)))
print("b:%s" % str(id(b)))

c = copy.deepcopy(a)
print("---------深拷贝----------")
print("a:%s" % str(id(a)))
print("c:%s" % str(id(c)))

print("---------验证(向a中添加一个44)----------")
a.append(44)

print("a:%s" % str(a))
print("b:%s" % str(b))
print("c:%s" % str(c))
