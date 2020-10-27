import time


def a():
    while True:
        print("---A---")
        yield
        time.sleep(0.1)


def b(a):
    while True:
        print("---B---")
        a.__next__()
        time.sleep(0.1)


if __name__ == '__main__':
    a = a()
    b(a)
