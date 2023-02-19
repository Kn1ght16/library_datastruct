from node import Node
from stack import Stack
import unittest


class Test_Node(unittest.TestCase):
    def test_node__init__(self):
        self.node_1 = Node(1)
        self.assertIs(self.node_1.data, Node(1).data)
        self.node_5 = Node(5, 1)
        self.assertIs(self.node_5.data, Node(5).data)

    def test_next_node(self):
        self.node_1 = Node(1)
        self.node_2 = Node(2, self.node_1)
        self.assertEqual(self.node_2.next_node, self.node_1)


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
        self.assertEqual(len(self.stack.datas), 2)
