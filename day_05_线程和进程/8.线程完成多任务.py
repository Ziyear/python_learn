import time
from threading import Thread


def test():
    print("------test------")
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    for i in range(5):
        test()
    def_end = time.time()
    print("原始方法耗时%d" % (def_end - start))
    for i in range(5):
        thread = Thread(target=test)
        thread.start()
    print("线程方法耗时%d" % (time.time() - def_end))