class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        new_node = Node(key)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)
            
            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end= " ")
            self.inorder(node.right) 
    def preorder(self, node):
        if node:
            print(node.key, end= " ")
            self.preorder(node.left)
            self.preorder(node.right) 
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)   
            print(node.key, end= " ")              

if __name__ == "__main__":
    # Create tree
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    

    print("Inorder Traversal: ")
    tree.inorder(tree.root)   # Output: 4 2 5 1 3

    print("\nPreorder Traversal: ")
    tree.preorder(tree.root)  # Output: 1 2 4 5 3

    print("\nPostorder Traversal: ")
    tree.postorder(tree.root) # Output: 4 5 2 3 1           