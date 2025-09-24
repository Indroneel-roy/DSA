# problem Link : https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def in_order(node):
            if not node: # base case
                return 
            in_order(node.left)
            result.append(node.val)
            in_order(node.right)
        in_order(root)
        return result    
if __name__ == "__main__":
    obj = Solution()
    # Example 1
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(obj.inorderTraversal(root)) # return [1,3,2]
    # Example 2
    root = None
    print(obj.inorderTraversal(root)) # return []
    # Example 3
    root = TreeNode(1)
    print(obj.inorderTraversal(root)) # return [1]    
               