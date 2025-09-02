# Problem Link : https://leetcode.com/problems/subarray-sum-equals-k/description/
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        PrefixSum = { 0 : 1}
        for n in nums:
            currSum += n
            diff = currSum - k
            res += PrefixSum.get(diff, 0)
            PrefixSum[currSum] = 1 + PrefixSum.get(currSum, 0)
        return res    
if __name__ == "__main__":
    nums = [1,-1, 1, 1, 1, 1, -1, 1, 1]
    k = 3
    sol = Solution()
    print(sol.subarraySum(nums, k))