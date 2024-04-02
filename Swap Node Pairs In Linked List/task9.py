class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    start = Node(head)
    current = start

    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        second.next = first
        current.next = second
        current = current.next.next
    return start.next
