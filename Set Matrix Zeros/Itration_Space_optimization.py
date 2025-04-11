from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        Rows, Cols = len(matrix), len(matrix[0])
        RowZero = False
        #Determine which cols and rows need to be zeros
        for r in range(Rows):
            for c in range(Cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        RowZero = True
        for r in range(1, Rows):
            for c in range(1, Cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for i in range(Rows):
                matrix[i][0] = 0
        if RowZero:
            for i in range(Cols):
                matrix[0][i] = 0
if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s = Solution()
    s.setZeroes(matrix=matrix)
    print(matrix)