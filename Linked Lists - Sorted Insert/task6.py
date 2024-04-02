class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    current_node = head
    if current_node is None:
        return Node(data)
    while current_node is not None:
        if data > current_node.data:
            if (current_node.next is not None and data < current_node.next.data) or current_node.next is None:
                next_value = current_node.next
                current_node.next = Node(data)
                current_node.next.next = next_value
                return head
        elif data < current_node.data and current_node == head:
            first_node = Node(data)
            first_node.next = head
            return first_node
        current_node = current_node.next
    return head
