# Problem Link : https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1    
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0    
    sol = Solution()
    res = sol.search(nums, target)
    print(res)