a = [1, 2, 3]
b = [3, 4, 5, 6]

a.extend(b)
print("extend--->", a)
a.append(b)
print("append--->", a)

# extend---> [1, 2, 3, 3, 4, 5, 6]
# append---> [1, 2, 3, 3, 4, 5, 6, [3, 4, 5, 6]]
