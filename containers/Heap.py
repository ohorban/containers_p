from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    def __init__(self, xs=None):
        super().__init__()
        self.size = 0
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        if not node:
            return True
        ret = True
        if node.left and node.right:
            if (node.left.value >= node.value and
                    node.right.value >= node.value):
                ret = True
            else:
                ret = False
        if node.left:
            if node.left.value < node.value:
                return False
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            if node.right.value < node.value:
                return False
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        self.size += 1
        if self.root:
            position = '{0:b}'.format(self.size)[1:]
            self.root = Heap._insert(self.root, position, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, position, value):
        if position[0] == '0':
            if not node.left:
                node.left = Node(value)
            else:
                node.left = Heap._insert(node.left, position[1:], value)
        if position[0] == '1':
            if not node.right:
                node.right = Node(value)
            else:
                node.right = Heap._insert(node.right, position[1:], value)
        if position[0] == '0':
            if node.value > node.left.value:
                tempval = node.value
                node.value = node.left.value
                node.left.value = tempval
                return node
            else:
                return node
        if position[0] == '1':
            if node.value > node.right.value:
                tempval = node.value
                node.value = node.right.value
                node.right.value = tempval
                return node
            else:
                return node

    def insert_list(self, xs):
        for elm in xs:
            self.insert(elm)
        return

    def find_smallest(self):
        return self.root.value

    def remove_min(self):
        if self.root is None:
            return
        else:
            position = '{0:b}'.format(self.size)[1:]
            val, self.root = Heap._remove_bottom_right(self.root, position)
            self.size -= 1
            if self.root is None:
                return
            else:
                self.root.value = val
                self.root = Heap._trickle(self.root)
            return

    @staticmethod
    def _remove_bottom_right(node, position):
        value = None
        if len(position) == 0:
            return None, None
        if position[0] == '0':
            if len(position) == 1:
                value = node.left.value
                node.left = None
            else:
                value, node.left = Heap._remove_bottom_right(
                    node.left, position[1:])
        if position[0] == '1':
            if len(position) == 1:
                value = node.right.value
                node.right = None
            else:
                value, node.right = Heap._remove_bottom_right(
                    node.right, position[1:])
        return value, node

    @staticmethod
    def _trickle(node):
        if Heap._is_heap_satisfied(node):
            pass
        else:
            if not node.left and node.right:
                temp = node.value
                node.value = node.right.value
                node.right.value = temp
                node.right = Heap._trickle(node.right)
            elif node.left and not node.right:
                temp = node.value
                node.value = node.left.value
                node.left.value = temp
                node.left = Heap._trickle(node.left)
            elif node.left.value >= node.right.value:
                temp = node.value
                node.value = node.right.value
                node.right.value = temp
                node.right = Heap._trickle(node.right)
            elif node.left.value <= node.right.value:
                temp = node.value
                node.value = node.left.value
                node.left.value = temp
                node.left = Heap._trickle(node.left)
            else:
                pass
        return node
