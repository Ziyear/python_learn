class Deque(object):
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def remove_front(self):
        if self.__list:
            return self.__list.pop(0)
        else:
            return None

    def remove_rear(self):
        if self.__list:
            return self.__list.pop()
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    queue = Deque()
    queue.add_front(1)
    queue.add_front(2)
    queue.add_rear(3)
    queue.add_rear(4)
    print(queue.remove_rear())
    print(queue.remove_rear())
    print(queue.remove_front())
    print(queue.remove_front())
