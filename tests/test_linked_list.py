"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList
from src.queue import Node


class TestNodeInit(unittest.TestCase):

    def test__init__Node(self):
        new_node = Node('data')

        self.assertEqual(new_node.data, 'data')
        self.assertEqual(new_node.next_node, None)


class TestLinkedList(unittest.TestCase):

    def test__init__Node(self):
        ll = LinkedList()
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.next_node, None)

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})

        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})

    def test_to_list(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy343434'})
        ll.insert_at_end({'id': 2, 'username': 'rim.for'})
        ll.insert_at_end({'id': 3, 'username': 'rubin1'})

        lst = ll.to_list()
        self.assertEqual(lst[0], {'id': 1, 'username': 'lazzy343434'})
        self.assertEqual(lst[1], {'id': 2, 'username': 'rim.for'})
        self.assertEqual(lst[2], {'id': 3, 'username': 'rubin1'})

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy343434'})
        ll.insert_at_end({'id': 2, 'username': 'rim.for'})
        ll.insert_at_end({'id': 3, 'username': 'rubin1'})

        user_data = ll.get_data_by_id(2)
        self.assertEqual(user_data, {'id': 2, 'username': 'rim.for'})
