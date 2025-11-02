# problem link : https://leetcode.com/problems/min-cost-to-connect-all-points/
from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i : [] for i in range(len(points))} # [cost, index]
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([cost, j])
                adj[j].append([cost, i])
        res = 0
        minH = [[0, 0]]
        visit = set()
        while len(visit) < N:
            cost, n = heapq.heappop(minH)
            if n in visit:
                continue
            res += cost
            visit.add(n)
            for costNei, nei in adj[n]:
                if nei not in visit:
                    heapq.heappush(minH, [costNei, nei])
        return res                
                
if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    sol = Solution()
    print(sol.minCostConnectPoints(points))