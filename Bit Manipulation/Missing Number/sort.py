# Problem Link : https://leetcode.com/problems/missing-number/description/
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i
        return n    

if __name__ == "__main__":
    nums = [8,6,4,2,3,5,7,0,1]
    sol = Solution()
    res = sol.missingNumber(nums)
    print(res)                