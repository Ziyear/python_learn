from multiprocessing import Process
import os
import time

g_num = 100


def run_proc(name):
    global g_num
    g_num += 1
    print("-----%s-----g_num=%d" % (name, g_num))
    time.sleep(1)


if __name__ == '__main__':
    print('父进程%s' % os.getpid())
    p1 = Process(target=run_proc, args=('test1',))
    p2 = Process(target=run_proc, args=('test2',))
    print('子进程将开始')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('g_num=%d' % g_num)
    print('子进程结束')
