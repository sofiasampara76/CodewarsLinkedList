class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None or head.next is None:
        return head

    def reverse_recursive(current_node, prev_node):
        if current_node.next is None:
            current_node.next = prev_node
            return current_node
        else:
            next_node = current_node.next
            current_node.next = prev_node
            return reverse_recursive(next_node, current_node)

    reversed_head = reverse_recursive(head, None)
    return reversed_head
