import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(node, value):
    if node is None:
        return False
    
    if node.value == value:
        return True
    elif node.value > value:
        return contains(node.left, value)
    else:
        return contains(node.right, value)

# Example tree
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))
