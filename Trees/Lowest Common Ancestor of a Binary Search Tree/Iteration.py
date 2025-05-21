# Problem Link : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr    

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
# Helper function to find a node by value
def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

if __name__ == "__main__":
    root_vals = [6,2,8,0,4,7,9,None,None,3,5]
    root = build_tree(root_vals)
    p = find_node(root, 2)
    q = find_node(root, 8)
    sol = Solution()
    res = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {res.val}")