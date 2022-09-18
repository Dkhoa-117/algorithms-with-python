class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    def Insert(self, data):
        if data < self.data:
            if self.left:
                self.left.Insert(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right:
                self.right.Insert(data)
            else:
                self.right = Node(data)
    # ! Inorder Traversa [Left] -> [Root] -> [Right] !
    def InorderTraversal(self, root):
        res = []
        if root:
            res = root.InorderTraversal(root.left)
            res.append(root.data)
            res += root.InorderTraversal(root.right)
        return res
    # ! Preorder Traversa [Root] -> [Left] -> [Right] !
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += root.PreorderTraversal(root.left)
            res += root.PreorderTraversal(root.right)
        return res
    # ! Postorder Traversa [Left] -> [Right] -> [Root] !
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = root.PostorderTraversal(root.left)
            res += root.PostorderTraversal(root.right)
            res.append(root.data)
        return res 

root = Node(27)
root.Insert(14)
root.Insert(35)
root.Insert(10)
root.Insert(19)
root.Insert(31)
root.Insert(42)
# * Testing Inorder Traversal *
print("Inorder Traversal: ")
print(root.InorderTraversal(root))
# * Testing Preorder Traversal *
print("Preorder Traversal: ")
print(root.PreorderTraversal(root))
# * Testing PostorderTraversal *
print("Postorder Traversal: ")
print(root.PostorderTraversal(root))

