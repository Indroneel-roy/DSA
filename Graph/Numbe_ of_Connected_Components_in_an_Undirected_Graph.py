from typing import List
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            stack = [node]
            while stack:
                 curr = stack.pop()
                 if curr not in visited:
                    visited.add(curr)
                    stack.extend(graph[curr])

        visited = set()
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count  