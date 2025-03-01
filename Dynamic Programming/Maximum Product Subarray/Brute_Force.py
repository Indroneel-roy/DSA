from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            curr = nums[i]
            res = max(res, curr)
            for j in range(i+1, len(nums)):
                curr *= nums[j]
                res = max(res, curr)
        return res
if __name__ == "__main__":
    nums = [1,2,-3,4]   
    sol = Solution()
    print(sol.maxProduct(nums))              