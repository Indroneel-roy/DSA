# Problem Link : https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])
        l, r = 0, Rows*Cols - 1
        while l <= r:
            m = l + (r - l) // 2
            row = m // Cols
            col = m % Cols
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False                
# time complexity O(log(m*n))
if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3   
    sol = Solution()
    res = sol.searchMatrix(matrix, target)
    print(res)