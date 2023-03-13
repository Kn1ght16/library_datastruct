import unittest
from node import Node
from stack import Stack


class Test_Stack(unittest.TestCase):
    def test_stack__init__(self):
        self.node_1 = Node(1)
        self.assertEqual(Node(1).data, self.node_1.data)

    def test_push(self):
        self.stack = Stack()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.stack.push(self.node_1)
        self.stack.push(self.node_2)

    def test_pop(self):
        self.stack = Stack()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.stack.push(self.node_1)
        self.stack.push(self.node_2)
        self.stack.pop()
        self.assertEqual(self.stack.pop().data, self.node_1.data)
        self.assertIsNone(self.stack.pop())