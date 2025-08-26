# Problem Link : https://leetcode.com/problems/range-sum-query-2d-immutable/description/
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomright = self.sumMatrix[r2][c2]
        aboveRight = self.sumMatrix[r1 - 1][c2]
        bottomleft = self.sumMatrix[r2][c1 - 1]
        topleft = self.sumMatrix[r1 - 1][c1 - 1]
        return bottomright - aboveRight - bottomleft + topleft


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    
    obj = NumMatrix(matrix)
    print(obj.sumRegion(2, 1, 4, 3))  # Output: 8
    print(obj.sumRegion(1, 1, 2, 2))  # Output: 11
    print(obj.sumRegion(1, 2, 2, 4))  # Output: 12
