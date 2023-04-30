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
    stack.push("data1")
    # assert stack.top ==
    assert stack.size == 1
    stack.push("data2")
    assert stack.size == 2
    stack.push("data3")
    assert stack.size == 3


def test_pop():
    stack.pop()
    assert stack.size == 2
    stack.pop()
    assert stack.size == 1
    stack.pop()
    assert stack.size == 0


def test_pop1():
    stack.push('data1')
    data = stack.pop()
    assert stack.top is None
    assert data == 'data1'


def test_pop2():
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()
    assert stack.top.data == 'data1'
    assert stack.top.data == 'data1'
