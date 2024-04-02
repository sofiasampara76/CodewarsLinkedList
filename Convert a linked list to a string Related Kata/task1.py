class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    current_node = node
    string = ''
    while current_node is not None:
        string += str(current_node.data) + ' -> '
        current_node = current_node.next
    string += 'None'
    return string