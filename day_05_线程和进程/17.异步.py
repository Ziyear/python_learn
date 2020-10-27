import os
import time
from multiprocessing import Pool


def test():
    print("----进程池中的进程---- pid=%d,ppid=%d" % (os.getpid(), os.getppid()))
    for i in range(3):
        print("----%d----" % i)
        time.sleep(0.5)
    return "haha"


def test2(args):
    print("------callback func-----pid=%d" % os.getpid())
    print("------callback func-----args=%s" % args)


if __name__ == '__main__':
    pool = Pool(3)

    pool.apply_async(func=test, callback=test2)
    pool.close()
    pool.join()
    time.sleep(5)

    print("------主进程-pid=%d--------" % os.getpid())
