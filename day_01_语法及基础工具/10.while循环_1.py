# break 和 continue 使用
i = 1
while i <= 10:
    i += 1
    if i % 2 == 0:
        print("continue %d" % i)
        continue
    if i == 5:
        print("break %d" % i)
        break
