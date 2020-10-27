import threading
import time


class My_Thread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)
            print(msg)


if __name__ == '__main__':
    for i in range(5):
        t1 = My_Thread(name="t_" + str(i))
        t1.start()
