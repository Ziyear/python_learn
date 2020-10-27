class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
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

    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                pre = pre.next
                count += 1
            node = Node(item)
            # 将 node的下一个节点指向元插入位置的节点
            node.next = pre.next
            # 将原节点下一个指向 当前节点
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.__head
            pre = None
            while cur is not None:
                if item == cur.elem:
                    if self.__head == cur:
                        self.__head = cur.next
                        return True
                    else:
                        pre.next = cur.next
                        return True
                else:
                    pre = cur
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
    sll = SingleLinkList()
    print(sll.is_empty())
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(5)
    sll.add(10)
    sll.add(11)
    sll.append(5)
    sll.insert(100, 111)
    print(sll.length())
    sll.travel()
    print(sll.search(1111))
    print(sll.remove(10))
    sll.travel()
