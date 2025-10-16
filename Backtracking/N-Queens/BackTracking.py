# Problem Link : https://leetcode.com/problems/n-queens/description/
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        boards = [["."] * n for i in range(n)]
        res = []

        def backTracking(r):
            if r == n:
                copy = [''.join(row) for row in boards]
                res.append(copy)
                return 
            for c in range(n):  
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r-c)
                boards[r][c] = "Q"

                backTracking(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r-c)
                boards[r][c] = "."
        backTracking(0)
        return res    
if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.solveNQueens(n))