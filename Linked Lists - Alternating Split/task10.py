class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception()

    head_first = head
    head_second = head.next
    current_node = head

    while current_node and current_node.next:
        temp = current_node.next
        current_node.next = temp.next
        if temp.next and current_node.next.next:
            temp.next = current_node.next.next
        else:
            temp.next = None
            break
        current_node = current_node.next

    return Context(head_first, head_second)
