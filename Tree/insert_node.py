# Create Node
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

# *Testing*
# root = Node(10)
# root.Insert(11)
# root.Insert(12)
# root.Insert(1)
# root.Insert(8)

# root.PrintTree()
