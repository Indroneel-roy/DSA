# Problem Link : https://leetcode.com/problems/diameter-of-binary-tree/description/
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        # return hight of the tree not result
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right) #height
        dfs(root)
        return res        
##Helper function to create tree
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    index = 1

    while queue and index < len(nodes):
        node = queue.popleft()

        # Left child
        if index < len(nodes) and nodes[index] is not None:
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1

        # Right child
        if index < len(nodes) and nodes[index] is not None:
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1

    return root     
if __name__ == "__main__":
    root = [1,2,3,4,5]
    root = build_tree(root)
    sol = Solution()
    res = sol.diameterOfBinaryTree(root)
    print(res)
         