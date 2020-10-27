# windows 不支持 fork。。。。。
# import os
# import time
# from multiprocessing import Process
#
# ret = os.fork()
#
# if ret == 0:
#     while True:
#         print("------1------")
#         time.sleep(1)
# else:
#     while True:
#         print("------2------")
#         time.sleep(1)


from multiprocessing import Process
import os
import time


def run_proc(name):
    while True:
        print("-----%s-----" % name)
        time.sleep(1)


if __name__ == '__main__':
    print('父进程%s' % os.getpid())
    p1 = Process(target=run_proc, args=('test1',))
    p2 = Process(target=run_proc, args=('test2',))
    p3 = Process(target=run_proc, args=('test3',))
    print('子进程将开始')
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('子进程结束')
