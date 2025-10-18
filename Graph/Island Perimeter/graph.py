# Problme link : https://leetcode.com/problems/island-perimeter/
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        def DFS(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0 
            visit.add((i, j))
            perim = DFS(i, j + 1)
            perim += DFS(i + 1, j) 
            perim += DFS(i, j - 1)
            perim += DFS(i - 1, j)      
            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return DFS(i, j) 
if __name__ == "__main__":
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    sol = Solution()
    print(sol.islandPerimeter(grid))                