# Problem Link : https://leetcode.com/problems/4sum/description/
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, quad = [], []
        nums.sort()
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):    
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i + 1, target - nums[i])
                    quad.pop()
                return
            # base condiction    
            l, r = start, len(nums) - 1
            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum < target:
                    l += 1
                elif twoSum > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        kSum(4, 0, target)
        return res                                    
if __name__ == "__main__":
     nums = [1,0,-1,0,-2,2]
     target = 0
     sol = Solution()
     print(sol.fourSum(nums, target))