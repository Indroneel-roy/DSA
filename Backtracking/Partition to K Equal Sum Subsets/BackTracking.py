# Problem Link : https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)     
if __name__ == "__main__":
    nums = [4,3,2,3,5,2,1]
    k = 4
    sol = Solution()
    print(sol.canPartitionKSubsets(nums, k))    