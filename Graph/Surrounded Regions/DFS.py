# Problem Link : https://leetcode.com/problems/surrounded-regions/description/
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or board[r][c] != "O"):
                return
            board[r][c] = "I"
            capture(r+1, c) 
            capture(r-1, c) 
            capture(r, c+1) 
            capture(r, c-1)
        #replace edges "0" by "I"
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and  (r in [0, rows - 1] or c in [0, cols - 1])):
                    capture(r,c)
        # replace every surrounded region by "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"         
        # Again replace "I" by "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "I":
                    board[r][c] = "O"     
        return board           
    
if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol = Solution()
    sol.solve(board)
    print(board)     

       