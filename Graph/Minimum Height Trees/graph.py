# problem link : https://leetcode.com/problems/minimum-height-trees/description/
# Brute force solution

# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         adj = [[] for _ in range(n)]
#         for u, v in edges:
#             adj[u].append(v)
#             adj[v].append(u)
        
#         def dfs(node, parent):
#             hig = 0
#             for nei in adj[node]:
#                 if nei == parent:
#                     continue
#                 hig = max(hig, 1 + dfs(nei, node))
#             return hig
#         res = []
#         for i in range(n):
#             minHig = n
#             curHig = dfs(i, -1)
#             if curHig == minHig:
#                 res.append(i)
#             elif curHig < minHig:
#                 res = [i]
#                 minHig = curHig
#         return res      


    #   topological sorting
from typing import List
from collections import defaultdict, deque    

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:     
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        leaves_node = deque()
        edge_cnt = {}
        for src, nei  in adj.items():
            edge_cnt[src] = len(nei)
            if len(nei) == 1:
                leaves_node.append(src)       
        while leaves_node:
            if n <= 2:
                return list(leaves_node)
            for _ in range(len(leaves_node)):
                node = leaves_node.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves_node.append(nei)

if __name__ == "__main__":
    n = 4
    edges = [[1,0],[1,2],[1,3]]
    sol = Solution()
    print(sol.findMinHeightTrees(n, edges))                        