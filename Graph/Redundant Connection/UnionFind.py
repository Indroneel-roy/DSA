# problem Link : https://leetcode.com/problems/redundant-connection/description/
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [ i for i in range(N+1)]
        Rank = [1] * (N + 1)
        
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if Rank[p1] > Rank[p2]:
                par[p2] = p1
                Rank[p1] += Rank[p2]
            else:
                par[p1] = p2
                Rank[p2] += Rank[p1]
            return True    
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]         
if __name__ == "__main__":
    edges = [[1,2],[1,3],[2,3]]
    sol = Solution()
    print(sol.findRedundantConnection(edges))            