class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end = " ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.value, end = " ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end = " ")

root = None
n = int(input("Enter the number of entries: "))
for _ in range(n):
    data = input()
    root = insert(root, data)
print("Inorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)

        
