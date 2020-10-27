from threading import Thread
import time

# 线程之间共享全局变量
g_num = 100


def work_1():
    global g_num
    # 测试线程共享变量的可见性
    for i in range(1000000):
        g_num += 1
    # print("------- in work_1, g_num is %d ---------" % g_num)


def work_2():
    global g_num
    for i in range(1000000):
        g_num += 1
    # print("------- in work_2, g_num is %d ---------" % g_num)


print("------- thread start before, g_num is %d ---------" % g_num)

t1 = Thread(target=work_1)
t2 = Thread(target=work_2)
t1.start()
t2.start()
time.sleep(1)
print("------- thread start after, g_num is %d ---------" % g_num)
