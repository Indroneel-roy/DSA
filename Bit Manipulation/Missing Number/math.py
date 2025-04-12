# Problem Link : https://leetcode.com/problems/missing-number/description/
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n+1) // 2
        actual_sum = sum(nums)
        missing_number = expected_sum - actual_sum
        return missing_number

if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    sol = Solution()
    res = sol.missingNumber(nums)
    print(res)    