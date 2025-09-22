# problem Link : https://leetcode.com/problems/search-insert-position/
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l                
if __name__ == "__main__":
    obj = Solution()
    print(obj.searchInsert([1,3,5,6], 5)) # return 2
    print(obj.searchInsert([1,3,5,6], 2)) # return 1
    print(obj.searchInsert([1,3,5,6], 7)) # return 4
    print(obj.searchInsert([1,3,5,6], 0)) # return 0
    print(obj.searchInsert([1], 0))       # return 0        