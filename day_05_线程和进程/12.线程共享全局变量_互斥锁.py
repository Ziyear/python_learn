from threading import Thread, Lock
import time

# 线程之间共享全局变量
g_num = 0


def work_1():
    global g_num
    # 测试线程共享变量的可见性
    global g_flag
    # 尝试获取锁，如果获取到了，其他 mutex 将会阻塞
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    # 释放锁，其他线程可以获取锁
    mutex.release()


def work_2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()


print("------- thread start before, g_num is %d ---------" % g_num)

# 创建互斥锁
mutex = Lock()

t1 = Thread(target=work_1)
t2 = Thread(target=work_2)
t1.start()
t2.start()
time.sleep(1)
print("------- thread start after, g_num is %d ---------" % g_num)
