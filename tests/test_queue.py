"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Node, Queue


class TestNodeInit(unittest.TestCase):

    def test__init__Node(self):
        new_node = Node('data')

        self.assertEqual(new_node.data, 'data')
        self.assertEqual(new_node.next_node, None)


class TestQueue(unittest.TestCase):

    def test_init_Queue(self):
        queue = Queue()

        self.assertEqual(queue.size, 0)
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)

    def test_is_empty(self):
        queue = Queue()
        self.assertEqual(queue.head, None)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.dequeue()

        self.assertEqual(queue.head.data, 'data2')

    def test_str(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        queue.dequeue()
        self.assertEqual(queue.head.data, 'data2')
        queue.dequeue()
        self.assertEqual(queue.head.data, 'data3')
        queue.dequeue()
        self.assertEqual(queue.head, None)
