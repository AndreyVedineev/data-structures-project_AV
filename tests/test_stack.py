"""Здесь надо написать тесты с использованием unittest для модуля stack."""

from src.stack import Node, Stack

n1 = Node(5, None)
stack = Stack()


def test_n1_init():
    assert n1.data == 5
    assert n1.next_node is None


def test_stack_init():
    assert stack.top is None


def test_push():
    pass


def test_pop():
    assert stack.pop() == stack.top.data
