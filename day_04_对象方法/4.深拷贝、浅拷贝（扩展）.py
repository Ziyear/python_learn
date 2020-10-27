import copy

a = [11, 22, 33]
b = [44, 55, 66]
c = [a, b]
c_元组 = (a, b)

d = c

print("---------浅拷贝----------")
print("c:%s" % str(id(a)))
print("d:%s" % str(id(b)))

e_元组 = copy.copy(c_元组)
print("---------元组copy拷贝----------")
print("c_元组:%s" % str(id(c_元组)))
print("e_元组:%s" % str(id(e_元组)))

e = copy.copy(c)
print("---------copy拷贝----------")
print("c:%s" % str(id(c)))
print("e:%s" % str(id(e)))

f = copy.deepcopy(c)
print("---------deepcopy拷贝----------")
print("c:%s" % str(id(c)))
print("f:%s" % str(id(f)))

print("---------验证(向a中添加一个44)----------")
a.append(44)

print("c:%s" % str(c))
print("d:%s" % str(d))
print("e:%s" % str(e))
print("f:%s" % str(f))
