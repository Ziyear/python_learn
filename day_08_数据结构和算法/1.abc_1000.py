import time


# a+b+c=1000 并且 a^2+b^2 = c^2 (a,b,c 为自然数) 求出a，b，c可能的组合

# T(n) = k * g(n)
# T(n) = n^3 * 2
# T(n) = g(n)
def method_1():
    start_time = time.time()
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print("a=%d, b=%d, c=%d" % (a, b, c))
    end_time = time.time()
    print("use times:%d" % (end_time - start_time))


# T(n) = n * n * (1 + 1) = O(n^2)
def method_2():
    start_time = time.time()
    for a in range(1001):
        for b in range(1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print("a=%d, b=%d, c=%d" % (a, b, c))
    end_time = time.time()
    print("use times:%d" % (end_time - start_time))


def main():
    method_2()


if __name__ == '__main__':
    main()
