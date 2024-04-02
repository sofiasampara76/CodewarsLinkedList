class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    i = 0
    while node is not None:
        if i == index:
            return node
        i += 1
        node = node.next
    raise Exception()
  