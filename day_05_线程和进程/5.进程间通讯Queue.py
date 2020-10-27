from multiprocessing import Queue, Process
import time
import random


# 写数据
def write(q):
    for val in ['A', 'B', 'C']:
        print("Put '%s' to queue..." % val)
        q.put(val)
        time.sleep(random.random())


# 读数据
def read(q):
    while True:
        if not q.empty():
            val = q.get(True)
            print("Get '%s' from queue." % val)
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    # 创建一个队列
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动
    pw.start()
    pw.join()

    pr.start()
    pr.join()
