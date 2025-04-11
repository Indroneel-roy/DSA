from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []
        while (l < r and top < bottom):
            # visiting top row after visiting increase the value of top by 1
            for i in range(l, r):
                res.append(matrix[l][i])
            top += 1

            #Visiting the last columnh
            for i in range(top, bottom):
                res.append(matrix[i][r-1])
            r -= 1

            if not (l < r and top < bottom):
                break

            #Visithing bottom column
            for i in range(r-1, l-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            #Vishing left bottom to top left
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][l])
            l += 1
        return res        

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    s = Solution()
    result = s.spiralOrder(matrix)
    print(result)