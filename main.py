from utils.node import Node
from utils.stack import Stack
from utils.custom_queue import Queue
from utils.linked_list import LinkedList


def main():
    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)
    print(n2.data)
    print(n1)
    print(n2.next_node)

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    print(stack.top.data)
    print(stack.top.next_node.data)
    print(stack.top.next_node.next_node.data)
    print(stack.top.next_node.next_node.next_node)

    stack = Stack()
    stack.push('data1')
    data = stack.pop()

    # стэк стал пустой
    print(stack.top)

    # pop() удаляет элемент и возвращает данные удаленного элемента
    print(data)

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    # теперь последний элемента содержит данные data1
    print(stack.top.data)

    # данные удаленного элемента
    print(data)

    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    print(queue.head.data)
    print(queue.head.next_node.data)
    print(queue.tail.data)
    print(queue.tail.next_node)
    #print(queue.tail.next_node.data)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    ll.print_ll()

    ll = LinkedList()

    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})

# метод to_list()
    lst = ll.to_list()
    for item in lst: print(item)

# get_data_by_id()
    user_data = ll.get_data_by_id(3)
    print(user_data)

# работа блока try/except
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end('idusername')
    ll.insert_at_end([1, 2, 3])
    ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

    user_data = ll.get_data_by_id(2)
    print(user_data)

#if __name__ == "__main__":
main()
