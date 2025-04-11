from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):

                top, bottom = l, r
                #save top left value in topleft variable
                topleft = matrix[top][l + i]

                # move bottom left value to topleft
                matrix[top][l+i] = matrix[bottom-i][l]

                # move bottom right value to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                #move top right value to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                #move topleft to top right
                matrix[top+i][r] = topleft
            l += 1
            r -= 1    
if __name__ == "__main__":
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s = Solution()
    s.rotate(matrix)
    print(matrix)
                