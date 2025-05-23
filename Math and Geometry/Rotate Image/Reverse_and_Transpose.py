from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        matrix.reverse()
        
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s = Solution()
    s.rotate(matrix)
    print(matrix)                