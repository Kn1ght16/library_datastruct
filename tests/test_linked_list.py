import unittest
from utils.linked_list import LinkedList


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

    def test_to_list(self):
        self.ll.insert_beginning({'id': 1, 'name': 'John'})
        self.ll.insert_beginning({'id': 2, 'name': 'Jane'})
        self.ll.insert_beginning({'id': 3, 'name': 'Bob'})
        self.assertEqual(self.ll.to_list(), [{'id': 3, 'name': 'Bob'}, {'id': 2, 'name': 'Jane'}, {'id': 1, 'name': 'John'}])

    def test_get_data_by_id(self):
        self.ll.insert_beginning({'id': 1, 'name': 'John'})
        self.ll.insert_beginning({'id': 2, 'name': 'Jane'})
        self.ll.insert_beginning({'id': 3, 'name': 'Bob'})
        self.assertEqual(self.ll.get_data_by_id(2), {'id': 2, 'name': 'Jane'})