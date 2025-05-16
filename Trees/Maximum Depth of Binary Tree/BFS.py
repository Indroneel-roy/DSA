#Problem link : https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level          

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
    tree_list = [3, 9, 20, None, None, 15, 7]
    root = build_tree(tree_list)

    sol = Solution()
    print(sol.maxDepth(root))  # Output: 3          
                