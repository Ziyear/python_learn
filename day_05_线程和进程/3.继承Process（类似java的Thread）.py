import os
import time
from multiprocessing import Process


class My_Process(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        t_start = time.time()
        print('子进程(%s)开始执行,父进程为(%s)' % (os.getpid(), os.getppid()))

        time.sleep(self.interval)
        t_stop = time.time()
        print("(%s)子进程执行结束,耗时%f秒" % (os.getpid(), t_stop - t_start))
#主进程
if __name__ == "__main__":
    #主进程开始时间
    t_start = time.time()
    print("当前程序的进程id: (%s)"%os.getpid())
    #调用Download函数 p就是生成的一个子进程 2传给init魔术方法
    #每次实例化的时候就相当于实例化了一个进程
    p = My_Process(5)
    p.start()
    #一直阻塞到子进程执行完 才开始执行主进程 实现进程同步
    #判断是否进程是否还在执行 True or False
    print(p.is_alive())
    p.join(2)
    if p.is_alive() == True:
        #等待子进程2秒 过时立即终止子进程p
        p.terminate()
        time.sleep(0.1)
    print(p.is_alive())
    t_stop = time.time()
    print("(%s)主进程执行结束,耗时%f秒" % (os.getpid(), t_stop - t_start))
