#Problem Link : https://leetcode.com/problems/3sum/

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums): # time complexity here O(n)
            if i > 0 and a == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r: # time complexity here O(n) Thus total time complexity is O(n*2) and space complexity O(1) or O(n) according to sorting technique
                ThreeSum = a + nums[l] + nums[r]
                if ThreeSum > 0:
                    r -= 1
                elif ThreeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res     

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    res = sol.threeSum(nums)
    print(res)    