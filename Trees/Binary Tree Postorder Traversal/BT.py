# Problem link : https://leetcode.com/problems/binary-tree-postorder-traversal/description/
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def post_order(node):
            if not node:
                return
            post_order(node.left)
            post_order(node.right)
            result.append(node.val)
        post_order(root)
        return result    
if __name__ == "__main__":
    obj = Solution()
    # Example 1
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(obj.postorderTraversal(root)) # return [3,2,1]
    # Example 2
    root = None
    print(obj.postorderTraversal(root)) # return []
    # Example 3
    root = TreeNode(1)
    print(obj.postorderTraversal(root)) # return [1]        
        