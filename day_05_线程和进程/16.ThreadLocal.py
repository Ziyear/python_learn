import threading

threading_local = threading.local()


def process_student():
    std = threading_local.student
    print("hello %s (in %s)" % (std, threading.current_thread().name))


def process_thread(name):
    threading_local.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=("super-ziyear",), name="t-1")
t2 = threading.Thread(target=process_thread, args=("sir zhao",), name="t-2")

t1.start()
t2.start()
t1.join()
t2.join()
