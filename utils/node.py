class Node():
    """Класс узла `Node`, содержащий два атрибута:
    - данные (любые полезные данные: число, строка, список и т.д.)
    - ссылка на следующий узел
    """

    def __init__(self, data, next=None):
        self.data = data
        self.next_node = next
