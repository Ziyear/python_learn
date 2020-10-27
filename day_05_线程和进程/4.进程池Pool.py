from multiprocessing import Pool
import os
import time
import random


def worker(name):
    t_start = time.time()
    print("%s开始执行，进程编号为%d" % (name, os.getpid()))
    time.sleep(random.random() * 5)
    t_stop = time.time()
    print("%s执行完毕，进程编号为%d，耗时%0.2f" % (name, os.getpid(), t_stop - t_start))


if __name__ == '__main__':
    po = Pool(3)  # 定义一个进程池 最大进程数为3
    for i in range(0, 10):
        # 阻塞方式
        # po.apply(worker, ("任务%d" % i,))
        # 异步阻塞  每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker, ("任务%d" % i,))

    print("-----start-----")
    # 关闭进程池，不再接受新的请求
    po.close()
    # 等待进程池中的所有子进程执行结束，必须放在close后边
    po.join()
    print("-----end-----")
