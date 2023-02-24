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

    def __repr__(self) -> str:
        """Возвращает атрибуты в понятном виде"""
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return f"{text[:-2]}"

    def push(self, data) -> Node:
        """push: добавить элемент в стек"""
        if len(self.datas) == 0:
            new_node = Node(data)
        else:
            new_node = Node(data, self.top)
        self.top = new_node
        return self.datas.append(new_node)

    def pop(self) -> Node:
        """pop: удалить  последний элемент из стека"""
        if len(self.datas) == 0:
            self.top = None
        elif len(self.datas) == 1:
            new_node = self.top
            self.top = None
            self.datas.pop()
            return new_node.data
        else:
            new_node = self.top
            self.top = self.datas[len(self.datas) - 2]
            self.datas.pop()
            return new_node.data
