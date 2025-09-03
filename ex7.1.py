class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    def insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end = " ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.value, end = " ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end = " ")

bst = BinaryTree()
root = None
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input())
    root = bst.insert(root, data)
print("Inorder Traversal:")
bst.inorder(root)
print("\nPreorder Traversal:")
bst.preorder(root)
print("\nPostorder Traversal:")
bst.postorder(root)
val = int(input("\nEnter value to search: "))
result = bst.search(root, val)
if result:
    print(f"{val} found in the tree.")
else:
    print(f"{val} not found in the tree.")
print("Height of the tree: ",bst.height(root))

        
