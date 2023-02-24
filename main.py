from utils.node import Node
from utils.stack import Stack


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


if __name__ == "__main__":
    main()
