# Problem Link : https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i >= len(nums):
                return total
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total) 
        return dfs(0, 0)       

if __name__ == "__main__":
    obj = Solution()
    # Example 1
    nums = [1,3]
    print(obj.subsetXORSum(nums)) # return 6
    # Example 2
    nums = [5,1,6]
    print(obj.subsetXORSum(nums)) # return 28
    # Example 3
    nums = [3,4,5,6,7,8]
    print(obj.subsetXORSum(nums)) # return 480