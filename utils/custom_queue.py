from node import Node


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

    def dequeue(self):
        if self.head is None:
            return None
        dequeue_element = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return dequeue_element.data