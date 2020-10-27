def test():
    i = 0
    while i < 5:
        if i == 0:
            temp = yield i
        else:
            yield i
        i += 1
t = test()
print(t.__next__())

print(t.send("hha"))