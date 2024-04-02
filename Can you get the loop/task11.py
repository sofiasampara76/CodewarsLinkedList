class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def loop_size(node):
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = node
            point1 = fast

            while fast != slow:
                fast = fast.next
                slow = slow.next

            start = slow

            fast = point1
            slow = node

            while fast.next != slow.next:
                fast = fast.next
                slow = slow.next

            end = fast

            counter = 1
            current_node = start

            while current_node != end:
                counter += 1
                current_node = current_node.next
            return counter
    return 0
            
