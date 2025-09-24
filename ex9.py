class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    return node.height if node else 0


def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0


def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x


def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        print("Duplicate values not allowed!")
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Left Left
    if balance > 1 and value < root.left.value:
        return right_rotate(root)
    # Right Right
    if balance < -1 and value > root.right.value:
        return left_rotate(root)
    # Left Right
    if balance > 1 and value > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right Left
    if balance < -1 and value < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def get_min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = get_min_value_node(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Left Left
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    # Left Right
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right Right
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    # Right Left
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def search(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    elif value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)

root = None
n = int(input("Enter number of values to insert: "))
for _ in range(n):
    val = int(input("Enter value: "))
    root = insert(root, val)
print("\nInorder Traversal:")
inorder(root)
print("\nTotal nodes:", count(root))
val = int(input("\nEnter value to search: "))
print("Found!" if search(root, val) else "Not Found!")
val = int(input("\nEnter value to delete: "))
root = delete(root, val)
print("\nInorder Traversal after Deletion:")
inorder(root)
print("\nTotal nodes:", count(root))
