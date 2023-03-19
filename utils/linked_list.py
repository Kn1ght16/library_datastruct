from utils.node import Node


class LinkedList():
    def __init__(self, begin=None, end=None):
        self.begin = begin
        self.end = end

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.begin is None:
            self.begin = new_node
        else:
            new_node.next_node = self.begin
            self.begin = new_node
        if self.end is None:
            self.end = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.end is None:
            self.end = new_node
        else:
            self.end.next_node = new_node
            self.end = new_node
        if self.begin is None:
            self.begin = new_node

    def print_ll(self):
        ll_string = ''
        node = self.begin
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)

    def to_list(self):
        ll_obj = []
        ll_data = []
        if self.begin is not None:
            ll_obj.append(self.begin)
        else:
            return ll_data
        while True:
            if ll_obj[len(ll_obj) - 1].next_node is None:
                break
            else:
                ll_obj.append(ll_obj[len(ll_obj) - 1].next_node)
        for obj in ll_obj:
            ll_data.append(obj.data)
        return ll_data

    def get_data_by_id(self, id):
        try:
            ll_data = self.to_list()
            for data in ll_data:
                if data['id'] == id:
                    return data
        except TypeError:
            print(f'Данные не являются словарем или в словаре нет id {id}')
