from node import Node


class Stack:
    """Стэк (Stack) — структура данных, представляющая из себя упорядоченный набор элементов, в которой добавление
    новых элементов и удаление существующих производится с одного конца, называемого вершиной стека. Притом первым из
    стека удаляется элемент, который был помещен туда последним, то есть в стеке реализуется стратегия «последним
    вошел — первым вышел» (last-in, first-out — LIFO). """

    def __init__(self) -> None:
        """инициализация пустого стэка"""
        self.datas = []
        """top— последний элемент в стэке"""
        self.top = None

    def push(self, data) -> Node:
        """функция добавляет элемент в  стэк"""
        if len(self.datas) == 0:
            new_node = Node(data)
        else:
            new_node = Node(data, self.top)
        self.top = new_node
        return self.datas.append(new_node)
