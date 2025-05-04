from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            l, r = 0, len(nums) - 1
            while l <= r: 
                mid = l + (r - 1) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return True
            return False
                            
if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3   
    sol = Solution()
    res = sol.searchMatrix(matrix, target)
    print(res)                         