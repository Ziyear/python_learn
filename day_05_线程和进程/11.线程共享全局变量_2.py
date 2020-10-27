from threading import Thread
import time

# 线程之间共享全局变量
g_num = 0

g_flag = 1


def work_1():
    global g_num
    # 测试线程共享变量的可见性
    global g_flag
    if g_flag == 1:
        for i in range(1000000):
            g_num += 1
        g_flag = 0


def work_2():
    global g_num
    while True:
        if g_flag != 1:
            for i in range(1000000):
                g_num += 1
            break


print("------- thread start before, g_num is %d ---------" % g_num)

t1 = Thread(target=work_1)
t2 = Thread(target=work_2)
t1.start()
t2.start()
time.sleep(1)
print("------- thread start after, g_num is %d ---------" % g_num)
