from insert_node import Node

def SearchNode(root, val):
    if root is None or root.data == val:
        return bool(root)
    if root.data < val:
        return bool(SearchNode(root.right, val))
    else:
        return bool(SearchNode(root.left, val))

root = Node(10)
root.Insert(11)
root.Insert(12)
root.Insert(1)
root.Insert(8)

print(SearchNode(root, 9))