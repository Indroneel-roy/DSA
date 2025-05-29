# Problem Link : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 : ], inorder[mid + 1 : ])
        return root
        
# Helper to print tree (inorder)
def print_inorder(node: Optional[TreeNode]):
    if node:
        print_inorder(node.left)
        print(node.val, end=' ')
        print_inorder(node.right)

if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    sol = Solution()
    tree = sol.buildTree(preorder, inorder)
    # print(tree)
    print("Inorder of constructed tree:")
    print_inorder(tree)
    print()