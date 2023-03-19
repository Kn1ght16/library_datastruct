import unittest
from utils.node import Node


class Test_Node(unittest.TestCase):
    def test_node__init__(self):
        self.node_1 = Node(1)
        self.assertIs(self.node_1.data, Node(1, None).data)
        self.node_5 = Node("abc", 1)
        self.assertEqual(self.node_5.data, Node("abc", 1).data)

    def test_next_node(self):
        self.node_1 = Node(1)
        self.node_2 = Node(2, self.node_1)
        self.assertEqual(self.node_2.next_node, self.node_1)

