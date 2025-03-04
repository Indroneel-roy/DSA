from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)     

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 2, 3]
    sol = Solution()
    print(sol.lengthOfLIS(nums))    