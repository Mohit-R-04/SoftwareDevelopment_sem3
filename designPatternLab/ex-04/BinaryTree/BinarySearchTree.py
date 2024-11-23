from .BinaryTree import BinaryTree
from .Node import Node

class BinarySearchTree(BinaryTree):
    def create_tree(self, elements):
        for element in elements:
            self.insert(element)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def traverse(self, order):
        if order == 'inorder':
            return self._inorder_traversal(self.root, [])
        elif order == 'preorder':
            return self._preorder_traversal(self.root, [])
        elif order == 'postorder':
            return self._postorder_traversal(self.root, [])
        else:
            raise ValueError("Traversal order must be 'inorder', 'preorder', or 'postorder'")

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)
        return result

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
        return result

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)
        return result
