class Node(object):

    def __init__(self, item):
        self.elem = item
        self.l_child = None
        self.r_child = None


class Tree(object):

    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)

            if cur_node.l_child is None:
                cur_node.l_child = node
                return
            else:
                queue.append(cur_node.l_child)

            if cur_node.r_child is None:
                cur_node.r_child = node
                return
            else:
                queue.append(cur_node.r_child)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.l_child is not None:
                queue.append(cur_node.l_child)
            if cur_node.r_child is not None:
                queue.append(cur_node.r_child)

    def pre_order(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.pre_order(node.l_child)
        self.pre_order(node.r_child)

    def in_order(self, node):
        """中序遍历"""
        if node is None:
            return
        self.in_order(node.l_child)
        print(node.elem, end=" ")
        self.in_order(node.r_child)

    def post_order(self, node):
        """后序遍历"""
        if node is None:
            return
        self.post_order(node.l_child)
        self.post_order(node.r_child)
        print(node.elem, end=" ")


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print("####### 层级 ########")
    tree.breadth_travel()
    print()
    print("####### 前序 ########")
    tree.pre_order(tree.root)
    print()
    print("####### 中序 ########")
    tree.in_order(tree.root)
    print()
    print("####### 后序 ########")
    tree.post_order(tree.root)