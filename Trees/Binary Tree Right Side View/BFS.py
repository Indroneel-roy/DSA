# Problem Link : https://leetcode.com/problems/binary-tree-right-side-view/description/
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)
        while q:
            qLen = len(q)
            RightSide = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    RightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if RightSide:
                res.append(RightSide.val)
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
    tree_list = [1,2,3,4,None,None,None,5]
    root = build_tree(tree_list)

    sol = Solution()
    print(sol.rightSideView(root))  # Output: 3                            

