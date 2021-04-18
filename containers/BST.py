from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    def __init__(self, xs=None):
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __eq__(self, t2):
        list1 = BinaryTree.to_list(self, 'inorder')
        list2 = BinaryTree.to_list(t2, 'inorder')
        return list1 == list2

    def is_bst_satisfied(self):
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            return BST._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        if node.value >= value:
            if node.left:
                BST._insert(value, node.left)
            else:
                node.left = Node(value)
                return
        elif node.value < value:
            if node.right:
                BST._insert(value, node.right)
            else:
                node.right = Node(value)
                return

    def insert_list(self, xs):
        for elm in xs:
            self.insert(elm)

    def __contains__(self, value):
        return self.find(value)

    def find(self, value):
        if self.root is None:
            return False
        else:
            return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        if node.value == value:
            return True
        if node.value > value:
            if node.left:
                return BST._find(value, node.left)
            else:
                return False
        elif node.value < value:
            if node.right:
                return BST._find(value, node.right)
            else:
                return False
        else:
            return False

    def find_smallest(self):
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        if self.root is None:
            return
        else:
            self.root = BST._remove(value, self.root)

    @staticmethod
    def _remove(value, node):
        if node is None:
            return node
        if value < node.value:
            node.left = BST._remove(value, node.left)
            return node
        elif value > node.value:
            node.right = BST._remove(value, node.right)
            return node
        if node.value == value:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                minval = BST._find_smallest(node.right)
                node.value = minval
                node.right = BST._remove(minval, node.right)
                return node

    def remove_list(self, xs):
        for elm in xs:
            self.remove(elm)
