import unittest
from node import Node
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.ll.insert_beginning(5)
        self.assertEqual(self.ll.begin.data, 5)
        self.assertEqual(self.ll.end.data, 5)
        self.ll.insert_beginning(10)
        self.assertEqual(self.ll.begin.data, 10)
        self.assertEqual(self.ll.end.data, 5)

    def test_linked_list_insert_at_end_empty(self):
        self.ll.insert_at_end(5)
        self.assertEqual(self.ll.begin.data, 5)
        self.assertEqual(self.ll.end.data, 5)
        self.ll.insert_at_end(10)
        self.assertEqual(self.ll.begin.data, 5)
        self.assertEqual(self.ll.end.data, 10)
