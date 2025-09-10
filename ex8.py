import sys
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key 
            root.right = self.delete(root.right, temp.key)  
        return root

    def minValueNode(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end = " ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end = " ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end = " ")

bst = BinarySearchTree()
root = None
while True:
    try:
        print("\n****** BST LOG BOOK ****** \n1.Insert Log Entry \n2.Traverse Log Entries \n3.Search Log Entry \n4.Delete Log Entry \n5.Count Entries \n6.Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            n = int(input("Enter the number of entries: "))
            for _ in range(n):
                data = input()
                root = bst.insert(root, data)
        elif choice == 2:
            print("Inorder Traversal:")
            bst.inorder(root)
            print("\nPreorder Traversal:")
            bst.preorder(root)
            print("\nPostorder Traversal:")
            bst.postorder(root)
            print("\n")
        elif choice == 3:
            val = input("\nEnter Vistor name to search: ")
            result = bst.search(root, val)
            if result:
                print(f"{val} found in the tree.")
            else:
                print(f"{val} not found in the tree.")
        elif choice == 4:
            val_to_delete = input("\nEnter key to be deleted: ")
            bst.delete(root, val_to_delete)
            print("Entry deleted successfully.");
        elif choice == 5:
            print("\nNo. of entries in Log Book: ",bst.count_nodes(root))
        elif choice == 6:
            print("Exiting Log Book....")
            sys.exit(0)
        else:
            print("Invalid choice! Please enter a valid choice.")
    except ValueError:
        print("Invalid input! Please enter a valid number for choice.")
        
        



        
