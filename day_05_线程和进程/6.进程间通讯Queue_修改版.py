from multiprocessing import Manager, Pool
import time
import random
import os


# 写数据
def write(q):
    print("write start this pid：%d，parent pid：%d" % (os.getpid(), os.getppid()))
    for val in ['A', 'B', 'C']:
        print("write put '%s' to queue." % val)
        q.put(val)


# 读数据
def read(q):
    print("read start this pid：%d，parent pid：%d" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("read get '%s' from queue." % q.get(i))


if __name__ == '__main__':
    print("(%s) start" % os.getpid())
    # 创建一个队列
    q = Manager().Queue()
    po = Pool()
    po.apply(write,(q,))
    po.apply(read,(q,))

    po.close()
    po.join()
    print("(%s) end" % os.getpid())
