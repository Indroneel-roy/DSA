# Problem Link : https://leetcode.com/problems/path-with-minimum-effort/description/
from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visit = set()
        minHeap = [[0, 0, 0]] # (diff, r, c)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue

            visit.add((r,c))

            if (r, c) == (rows-1, cols-1):
                return diff
            

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or newR == rows or newC == cols or (newR, newC) in visit):
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])    
                
if __name__ == "__main__":
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    sol = Solution()
    print(sol.minimumEffortPath(heights))
