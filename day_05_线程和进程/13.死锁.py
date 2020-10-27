import threading
import time


class My_Thread_1(threading.Thread):

    def run(self):
        # 获取A锁，然后尝试获取B锁，
        if mutexA.acquire():
            print(self.name + " My_Thread_1--- UP --- ")
            time.sleep(1)

            if mutexB.acquire(blocking=True, timeout=2):
                print(self.name + " My_Thread_1--- DOWN --- ")
                mutexB.release()
            mutexA.release()


class My_Thread_2(threading.Thread):

    def run(self):
        # 获取B锁，然后尝试获取A锁，
        if mutexB.acquire():
            print(self.name + " My_Thread_2--- UP --- ")
            time.sleep(1)

            if mutexA.acquire(blocking=True, timeout=2):
                print(self.name + " My_Thread_2--- DOWN --- ")
                mutexA.release()
            mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    t1 = My_Thread_1()
    t2 = My_Thread_2()
    t1.start()
    t2.start()
