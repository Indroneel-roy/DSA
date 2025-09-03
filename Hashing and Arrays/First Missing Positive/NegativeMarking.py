# Problem Link : https://leetcode.com/problems/first-missing-positive/description/
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val-1] > 0:
                    nums[val - 1] *= -1       
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums) + 1) 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1                       
if __name__ == "__main__":
    nums = [3,2,1,-1,7,4,-5]    
    sol = Solution()
    print(sol.firstMissingPositive(nums))