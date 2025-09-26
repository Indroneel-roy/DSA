# Problem Link : https://leetcode.com/problems/binary-tree-preorder-traversal/description/
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def pre_order(node):
            if not node:
                return
            result.append(node.val)
            pre_order(node.left)
            pre_order(node.right)
        pre_order(root)
        return result
if __name__ == "__main__":
    obj = Solution()
    # Example 1
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(obj.preorderTraversal(root)) # return [1,2,3]
    # Example 2
    root = None
    print(obj.preorderTraversal(root)) # return []
    # Example 3
    root = TreeNode(1)
    print(obj.preorderTraversal(root)) # return [1]
        