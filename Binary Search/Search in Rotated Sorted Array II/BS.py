# Problem Link : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        return False                                    
if __name__ == "__main__":
    obj = Solution()
    print(obj.search([2,5,6,0,0,1,2], 0)) # return True
    print(obj.search([2,5,6,0,0,1,2], 3)) # return False
    print(obj.search([1,0,1,1,1], 0))     # return True
    print(obj.search([1,1,3,1], 3))       # return True
    print(obj.search([3,1], 1))           # return True