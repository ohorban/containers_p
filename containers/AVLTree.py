from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    def __init__(self, xs=None):
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def balance_factor(self):
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        if not node:
            return True
        ret = True
        balance_factor = AVLTree._balance_factor(node)
        if balance_factor >= -1 and balance_factor <= 1:
            ret = True
        else:
            ret = False
        if node.left:
            ret &= AVLTree._is_avl_satisfied(node.left)
        if node.right:
            ret &= AVLTree._is_avl_satisfied(node.right)
        return ret

    @staticmethod
    def _left_rotate(node):
        tempval = node.value
        tempright = node.right
        if tempright:
            templeft = tempright.left
        else:
            templeft = None
        node.value = tempright.value
        node.right = tempright.right
        tempright = node.left
        node.left = Node(tempval, tempright, templeft)
        return node

    @staticmethod
    def _right_rotate(node):
        tempval = node.value
        templeft = node.left
        if templeft:
            tempright = templeft.right
        else:
            tempright = None
        node.value = templeft.value
        node.left = templeft.left
        templeft = node.right
        node.right = Node(tempval, tempright, templeft)
        return node

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        if value == self.root.value:
            return
        else:
            self._insert(value, self.root)
            while not self.is_avl_satisfied():
                self.root = self.rebalance(self.root)
            return

    @staticmethod
    def _insert(value, node):
        if node.value == value:
            return
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return
            else:
                return AVLTree._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
                return
            else:
                return AVLTree._insert(value, node.right)

    def rebalance(self, node):
        if node is None:
            return
        if self._balance_factor(node) == -2 or self._balance_factor(node) == 2:
            node = self._rebalance(node)
        else:
            node.left = self.rebalance(node.left)
            node.right = self.rebalance(node.right)
        return node

    @staticmethod
    def _rebalance(node):
        if node is None:
            return
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
            return node
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
            return node
