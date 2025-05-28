class NodeTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    def __repr__(self):
        return repr(self.data)
    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self
    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self

def bst_insert(root, node):
    last_node = None
    current_node = root
    while current_node is not None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else: 
            current_node = current_node.right
    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)

    return root
def bst_create():
    root = NodeTree(10)
    for item in [5, 27, 3, 7, 12, 19, 1, 4]:
        node = NodeTree(item)
        root = bst_insert(root, node)
    return root
def in_order(node):
    if node.left:
        in_order(node.left)
    print(node) 
    if node.right:
        in_order(node.right)
    
def bst_minimum(root):
    while root.left is not None:
        root = root.left
    return root

def bst_transplant(root, current_node, new_node):
    if current_node.parent is None:
        root = new_node
    elif current_node.parent.left == current_node:
        current_node.parent.add_left(new_node)
    else:
        current_node.parent.add_right(new_node)
    if new_node is not None:
        new_node.parent = current_node.parent     
    return root
def bst_delete(root, node):
    if node.left is None:
        root = bst_transplant(root, node, node.right)
    elif node.right is None:
        root = bst_transplant(root, node, node.left)
    else:
        min_node = bst_minimum(node.right)
        if min_node.parent != node:
            root = bst_transplant(root, min_node, min_node.right)
            min_node.add_right(node.right)
        root = bst_transplant(root, node, min_node)
        min_node.add_left(node.left)
        
    return root                                                                               


#Helper to find a node by value
def bst_search(root, value):
    if root is None or root.data == value:
        return root
    if value < root.data:
        return bst_search(root.left, value)
    else:
        return bst_search(root.right, value)


# Main Driver Code
if __name__ == "__main__":
    root = bst_create()
    print("BST (in-order) before deletion:")
    in_order(root)
    print("\n")

    # Example: Delete node with value 5
    to_delete = bst_search(root, 5)
    if to_delete:
        root = bst_delete(root, to_delete)

    print("BST (in-order) after deleting 5:")
    in_order(root)
    print()