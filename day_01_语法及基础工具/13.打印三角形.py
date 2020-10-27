i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1

for i in range(10):
    for j in range(0, 10 - i):
        print(end=" ")
    for k in range(10 - i, 10):
        print("$", end=" ")

    print("")