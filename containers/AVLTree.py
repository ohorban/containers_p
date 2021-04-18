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
        tempNode = node
        newNode = tempNode.right
        tempNode.right = newNode.left
        newNode.left = tempNode
        return tempNode

    @staticmethod
    def _right_rotate(node):
        tempNode = node
        newNode = tempNode.left
        tempNode.left = newNode.right
        newNode.right = tempNode
        return tempNode

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            AVLTree._insert(value, self.root)
            self.rebalance(self.root)
            return

    @staticmethod
    def _insert(value, node):
        if node.value >= value:
            if node.left:
                AVLTree._insert(value, node.left)
            else:
                node.left = Node(value)
                return
        elif node.value < value:
            if node.right:
                AVLTree._insert(value, node.right)
            else:
                node.right = Node(value)
                return

    def rebalance(self, node):
        if not node:
            return
        if self._balance_factor(node) == -2 or self._balance_factor(node) == 2:
            node = AVLTree._rebalance(node)
        else:
            node.left = self.rebalance(node.left)
            node.right = self.rebalance(node.right)
        return node

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if node is None:
            return
        factor = AVLTree._balance_factor(node)
        if factor < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
            return node
        elif factor > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
            return node
