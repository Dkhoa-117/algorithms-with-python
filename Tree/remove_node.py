from insert_node import Node

def RemoveNode(root, val):
    # base case: not found
    if root is None:
        return root
    if root.data < val:
        root.right = RemoveNode(root.right, val)
    elif root.data > val:
        root.left = RemoveNode(root.left, val)
    # Found 
    else:
        if not root.left and not root.right:
            return None
        elif root.left and root.right:
            maxNode = FindMaxNode(root.left)
            root.data = maxNode.data
            RemoveNode(root.left, maxNode.val)
        else:
            child = root.right if root.right else root.left
            root = child
        return root
def FindMaxNode(root):
    if root.right:
        return FindMaxNode(root.right)
    return root

# *Testing*
root = Node(10)
root.Insert(11)
root.Insert(12)
root.Insert(1)
root.Insert(8)
print("before")
root.PrintTree()
RemoveNode(root, 11)
print("after")
root.PrintTree()
