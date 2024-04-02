class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current_node = head
    while current_node is not None:
        if current_node.next is not None and current_node.data == current_node.next.data:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return head

# linked = Node(1, Node(1, Node(1, Node(1))))
# new = remove_duplicates(linked)

# while new is not None:
#     print(new.data)
#     new = new.next
