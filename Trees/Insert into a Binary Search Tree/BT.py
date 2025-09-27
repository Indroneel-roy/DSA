# Problem Link : https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Iterative solution
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root:
        #     return TreeNode(val)
        # curr = root    
        # while True:
        #     if val > curr.val:
        #         if not curr.right:
        #             curr.right = TreeNode(val)
        #             return root
        #         curr = curr.right
        #     else:
        #         if not curr.left:
        #             curr.left = TreeNode(val)
        #             return root
        #         curr = curr.left   
# Recursive                 
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:           
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root      
if __name__ == "__main__":
    obj = Solution()
    # Example 1
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    val = 5
    new_root = obj.insertIntoBST(root, val)
    # The tree after insertion should be:
    #       4
    #      / \
    #     2   7
    #    / \   \
    #   1   3   5
    print(new_root.val) # return 4
    print(new_root.right.val) # return 7
    print(new_root.right.left.val) # return 5
    # Example 2
    root = None
    val = 5
    new_root = obj.insertIntoBST(root, val)
    print(new_root.val) # return 5
    # Example 3
    root = TreeNode(40)
    root.left = TreeNode(20)
    root.right = TreeNode(60)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(30)
    root.right.left = TreeNode(50)
    root.right.right = TreeNode(70)
    val = 25
    new_root = obj.insertIntoBST(root, val)
    # The tree after insertion should be:
    #        40
    #       /  \
    #     20    60
    #    / \   / \
    #   10 30 50 70
    #      /
    #     25
    print(new_root.val) # return 40
    print(new_root.left.val) # return 20
    print(new_root.left.right.val) # return 30
    print(new_root.left.right.left.val) # return 25           