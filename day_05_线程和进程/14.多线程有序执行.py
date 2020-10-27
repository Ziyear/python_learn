import threading
import time


class Task1(threading.Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("-----Task1-----")
                time.sleep(0.5)
                lock2.release()


class Task2(threading.Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("-----Task2-----")
                time.sleep(0.5)
                lock3.release()


class Task3(threading.Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("-----Task3-----")
                time.sleep(0.5)
                lock1.release()


lock1 = threading.Lock()

lock2 = threading.Lock()
lock2.acquire()
lock3 = threading.Lock()
lock3.acquire()

t1 = Task1()
t2 = Task2()
t3 = Task3()
t1.start()
t2.start()
t3.start()
