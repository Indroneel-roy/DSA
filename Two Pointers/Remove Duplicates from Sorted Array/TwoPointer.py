# problem link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1        
if __name__ == "__main__":
    sol  = Solution()
    nums = [1,1,2]
    print(sol.removeDuplicates(nums))