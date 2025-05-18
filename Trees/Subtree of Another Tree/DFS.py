# Problem Link : https://leetcode.com/problems/subtree-of-another-tree/description/
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root: 
            return False
        if self.SameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            

    def SameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        return (self.SameTree(root.left, subRoot.left) and (self.SameTree(root.right, subRoot.right)))
                
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
    root = [3,4,5,1,2]
    subRoot = [4,1,2]   
    p = build_tree(root)
    q = build_tree(subRoot)
    sol = Solution()
    res = sol.isSubtree(p, q)
    print(res)                