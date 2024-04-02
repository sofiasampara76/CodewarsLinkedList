class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    list_of_nodes = s.split(' -> ')
    if len(list_of_nodes) == 1:
        return None
    for i, data in enumerate(reversed(list_of_nodes[:-1])):
        if i == 0:
            current_node = Node(data, None)
        else:
            current_node = Node(data, current_node)
    return current_node

# node1 = linked_list_from_string("1 -> 2 -> 3 -> None")

# while node1 is not None:
#     print(node1.data)
#     node1 = node1.next
