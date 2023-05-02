"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Node, Stack


class TestNodeInit(unittest.TestCase):

    def test__init__(self):
        n1 = Node(5, None)

        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)


class TestSteak(unittest.TestCase):
    def test_stack_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

    def test_push(self):
        stack = Stack()
        stack.push("data1")
        self.assertEqual(stack.size, 1)
        self.assertEqual(stack.top.data, "data1")
        stack.push("data2")
        self.assertEqual(stack.size, 2)
        self.assertEqual(stack.top.data, "data2")
        stack.push("data3")
        self.assertEqual(stack.size, 3)
        self.assertEqual(stack.top.data, "data3")

    def test_pop(self):
        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        stack.push("data3")
        self.assertEqual(stack.top.data, "data3")
        stack.pop()
        self.assertEqual(stack.top.data, "data2")
        self.assertEqual(stack.size, 2)
        stack.pop()
        self.assertEqual(stack.top.data, "data1")
        self.assertEqual(stack.size, 1)
        stack.pop()
        self.assertEqual(stack.size, 0)

        with self.assertRaises(AttributeError):
            stack.pop()
            self.assertEqual(stack.size, 0)


if __name__ == '__main__':
    unittest.main()
