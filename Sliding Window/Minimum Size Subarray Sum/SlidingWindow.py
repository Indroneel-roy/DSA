# Problem Link : https://leetcode.com/problems/minimum-size-subarray-sum/description/
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float("inf")
        currSum = 0
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                currSum -= nums[left]
                min_len = min(min_len, right - left + 1)
                left += 1
        return 0 if min_len == float("inf") else min_len        
if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    sol = Solution()
    print(sol.minSubArrayLen(target, nums))    
