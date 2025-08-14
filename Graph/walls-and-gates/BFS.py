from typing import List
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addroom(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == -1 or (r,c) in visited):
                return
            visited.add((r,c))
            q.append([r,c])    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addroom(r+1, c)
                addroom(r-1, c)
                addroom(r, c+1)
                addroom(r, c-1)
            dist += 1   
if __name__ == "__main__":
    Input = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]    
    sol = Solution()
    sol.islandsAndTreasure(Input)
    print(Input)

             