# Problem Link : https://leetcode.com/problems/delete-node-in-a-bst/description/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            #find the min from right
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root    
    
if __name__ == "__main__":
    obj = Solution()
    # Example 1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    key = 3
    new_root = obj.deleteNode(root, key)
    # The tree after deletion should be:
    #       5
    #      / \
    #     4   6
    #    /     \
    #   2       7
    print(new_root.val) # return 5
    print(new_root.left.val) # return 4
    print(new_root.left.left.val) # return 2
    print(new_root.right.val) # return 6
    print(new_root.right.right.val) # return 7
    # Example 2
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    key = 0
    new_root = obj.deleteNode(root, key)
    # The tree after deletion should be same as input tree since key is not found:
    #       5
    #      / \
    #     3   6
    #    / \   \
    #   2   4   7
    print(new_root.val) # return 5
    print(new_root.left.val) # return 3
    print(new_root.left.left.val) # return 2
    print(new_root.left.right.val) # return 4
    print(new_root.right.val) # return 6
    print(new_root.right.right.val) # return 7
    # Example 3
    root = None
    key = 0
    new_root = obj.deleteNode(root, key)
    print(new_root) # return None                            
        