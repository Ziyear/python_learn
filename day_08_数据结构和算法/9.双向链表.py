class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        count = 0
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(str(cur.elem), end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """链表头部"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            # 获取插入位置的节点
            cur = self.__head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            node = Node(item)
            # 将 插入节点的下一个节点指向插入位置节点
            node.next = cur
            # 将 插入节点的上一个节点指向插入位置节点的上一个节点
            node.prev = cur.prev
            # 将插入位置节点上一个的下一个指向 插入节点
            cur.prev.next = node
            # 将插入位置节点上一个指向 插入节点
            cur.pre = node

    def remove(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur is not None:
                if item == cur.elem:
                    # 头节点
                    if self.__head == cur:
                        # 将头节点指向删除节点下一个节点
                        self.__head = cur.next
                        # 将向删除节下一个节点 的上一个节点指向头节点
                        if cur.next:
                            # 判断链表是否只有一个元素
                            # 如果存在下一个元素，则将下一个元素的上一个节点指向none ，及头元素
                            cur.next.prev = None
                        return True
                    else:
                        cur.prev.next = cur.next
                        if cur.next:
                            cur.next.prev = cur.prev
                        return True
                else:
                    cur = cur.next
        return False

    def search(self, item):
        if self.is_empty():
            return -1
        else:
            count = 0
            cur = self.__head
            while cur is not None:
                if item == cur.elem:
                    return count
                cur = cur.next
                count += 1
        return -1


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    dll.append(1)
    print(dll.remove(1))
    dll.append(2)
    dll.append(3)
    dll.append(5)
    dll.add(10)
    dll.add(11)
    dll.append(5)
    dll.insert(100, 111)
    print(dll.length())
    dll.travel()
    print(dll.search(1111))
    print(dll.remove(10))
    dll.travel()
    print(dll.remove(11))

    dll.travel()
