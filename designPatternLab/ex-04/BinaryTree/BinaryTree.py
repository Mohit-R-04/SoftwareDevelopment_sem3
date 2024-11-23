from abc import ABC, abstractmethod
from .Node import Node

class BinaryTree(ABC):
    def __init__(self):
        self.root = None

    @abstractmethod
    def create_tree(self, elements):
        pass

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def traverse(self, order):
        pass
