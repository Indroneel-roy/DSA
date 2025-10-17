# Problem Link : https://leetcode.com/problems/n-queens-ii/description/
from typing import List
class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()
        boards = [["."] * n for i in range(n)]
        res = 0

        def backTracking(r):
            nonlocal res
            if r == n:
                res += 1
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
    print(sol.totalNQueens(n))    