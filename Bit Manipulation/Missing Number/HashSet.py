# Problem Link : https://leetcode.com/problems/missing-number/description/
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        for i in range(n + 1):
            if i not in num_set:
                return i
if __name__ == "__main__":
    nums = [8,6,4,2,3,5,7,0,1]
    sol = Solution()
    res = sol.missingNumber(nums)
    print(res)                