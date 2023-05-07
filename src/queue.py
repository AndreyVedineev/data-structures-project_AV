class Node:
    """Класс для узла очереди"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            new_node.next_node = self.head
            self.head = new_node
            self.tail = self.head

        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next_node
            self.size -= 1
            if self.head is None:
                self.tail = None
            return data
        else:
            return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return f"Пусто"
        return self.head.data

