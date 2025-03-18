class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.data = None


    def insert(self, value,data=None):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.data = data
            else:
                self.left.insert(value,data)
        else:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.data = data
            else:
                self.right.insert(value, data)

#-----------------------------------------------------------------------------------------------------------------------

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

#-----------------------------------------------------------------------------------------------------------------------

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.value)

# -----------------------------------------------------------------------------------------------------------------------

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

# -----------------------------------------------------------------------------------------------------------------------

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self


tree = TreeNode(8)

tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(6,{"data":"Hello World"})
tree.insert(5)
tree.insert(7)
tree.insert(12)
tree.insert(10)
tree.insert(9)
tree.insert(11)
tree.insert(14)
tree.insert(13)
tree.insert(15)

tree.inorder_traversal()

print(tree.find(6).data["data"])
