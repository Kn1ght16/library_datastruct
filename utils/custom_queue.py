class Node():
    """Класс узла `Node`, содержащий два атрибута:
    - данные (любые полезные данные: число, строка, список и т.д.)
    - ссылка на следующий узел"""
    def __init__(self, data, next=None):
        self.data = data
        self.next_node = next


class Queue:
    """Экземпляр класса Queue инициализируется двумя атрибутами,
     хранящими ссылки на начало и конец очереди.
      Для пустой очереди оба эти атрибута равны None."""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Метод для добавления данных в очередь"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
