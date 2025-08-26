# Problem Link : https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res        
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 10]
    sol = Solution()
    print(sol.productExceptSelf(nums))    