#Problem Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
       
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
            
                r = mid
            else:
                l = mid + 1
        return nums[l]         
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    sol = Solution()
    res = sol.findMin(nums)
    print(res)        