class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""

        self.top = None
        self.size = 0  # глубина стека

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """

        new_node = Node(data, None)  # создаем экземпляр класса Node, нижний элемент стека
        if self.top:  # проверка есть предыдущий (нижний) элемент стека? если есть
            new_node.next_node = self.top  # тогда записывает в атрибут верхнего(нового) элемента стека историю нижних элеметов
        self.top = new_node # иначе созданный экземпяр класса Node становитья верхним.
        self.size += 1

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента - по типу метода list.pop

        """

        temp = self.top.data # сохраняем временно верхний элемент стека
        self.top = self.top.next_node  # назначаем предыдущий элемент верхним
        self.size -= 1
        return temp # возвращаем верхний элемент и забываем про него

    def peek(self):
        """Для доступа к верхней записи данных в стеке без изменения самого стека"""
        return self.top.data
