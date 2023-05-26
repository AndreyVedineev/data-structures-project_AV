class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):

        self.head = None
        self.next_node = None

    def insert_beginning(self, data: dict):
        """Принимает; данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next_node is not None:
                n = n.next_node
            n.next_node = new_node

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке"""
        lst = []
        current_node = self.head
        while current_node is not None:
            lst.append(current_node.data)
            current_node = current_node.next_node
        return lst

    def get_data_by_id(self, parm):
        """возвращает первый найденный в словарь с ключом 'id', значение которого равно переданному в метод
        значению."""

        current_node = self.head
        while current_node is not None:
            try:
                if parm == current_node.data['id']:
                    return current_node.data
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
            current_node = current_node.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
