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

    def test_insert_at_end(self):
        ll = LinkedList()

        # Добавляем данные
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.head, {'id': 2})
        ll.insert_at_end({'id': 3})

