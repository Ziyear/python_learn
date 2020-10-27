class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单向循环链表"""

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(str(cur.elem), end=" ")
            cur = cur.next
        # 退出循环 cur 指向尾节点 但尾节点未打印
        print(str(cur.elem))

    def add(self, item):
        """链表头部"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 找到尾节点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 将头节点指向新节点,并将尾节点指向头节点
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self, item):
        """链表尾部"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 找到尾节点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 尾节点指向 插入的节点，并将插入的节点指向头节点
            cur.next = node
            node.next = self.__head

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
            # 只有一个节点
            if self.__head == cur.next:
                self.__head.next = None
                self.__head = None
                return True

            while cur.next != self.__head:
                if item == cur.elem:
                    # 头节点
                    if self.__head == cur:
                        # 找尾节点
                        rear = self.__head
                        while rear.next != self.__head:
                            rear = rear.next
                        self.__head = cur.next
                        rear.next = self.__head
                        return True
                    else:
                        # 中间节点
                        pre.next = cur.next
                        return True
                else:
                    pre = cur
                    cur = cur.next
            # 尾节点 （并且不止一个节点）
            if item == cur.elem:
                cur.next = None
                pre.next = self.__head
                return True

        return False

    def search(self, item):
        if self.is_empty():
            return -1
        else:
            count = 0
            cur = self.__head
            # 只有一个节点时
            if cur.next == self.__head and item == cur.elem:
                return count
            while cur.next != self.__head:
                if item == cur.elem:
                    return count
                cur = cur.next
                count += 1
            if item == cur.elem:
                return count
        return -1


if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())
    sll.append(1)
    print(sll.remove(1))
    sll.append(2)
    sll.append(3)
    sll.append(5)
    sll.append(1)
    sll.add(10)
    sll.add(11)
    sll.append(5)
    sll.insert(100, 111)
    print(sll.length())
    sll.travel()
    print(sll.search(1))
    print(sll.remove(10))
    sll.travel()
