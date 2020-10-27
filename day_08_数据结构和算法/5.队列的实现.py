class Queue(object):
    def __init__(self):
        self.__list = []

    def en_queue(self, item):
        self.__list.append(item)

    def de_queue(self):
        if self.__list:
            return self.__list.pop(0)
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    queue = Queue()
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    queue.en_queue(4)
    print(queue.de_queue())
    print(queue.de_queue())
    print(queue.de_queue())
    print(queue.de_queue())