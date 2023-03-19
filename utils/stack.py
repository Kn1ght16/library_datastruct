from utils.node import Node


class Stack:
    """Стэк (Stack) — структура данных, представляющая из себя упорядоченный набор элементов, в которой добавление
    новых элементов и удаление существующих производится с одного конца, называемого вершиной стека. Притом первым из
    стека удаляется элемент, который был помещен туда последним, то есть в стеке реализуется стратегия «последним
    вошел — первым вышел» (last-in, first-out — LIFO). """

    def __init__(self) -> None:
        """top— последний элемент в стэке"""
        self.top = None

    def __repr__(self) -> str:
        """Возвращает атрибуты в понятном виде"""
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return f"{text[:-2]}"

    def push(self, data) -> None:
        """push: добавить элемент в стек"""
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self) -> Node:
        """pop: удалить  последний элемент из стека"""
        if self.top is None:
            return None
        removed_data = self.top.data
        self.top = self.top.next_node
        return removed_data
