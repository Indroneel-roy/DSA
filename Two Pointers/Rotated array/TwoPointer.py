# Problem Link : https://neetcode.io/problems/rotate-array?list=neetcode250
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def helper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        #reverse whole array
        helper(l=0, r = len(nums) - 1)
        #reverse first k elements
        helper(l=0, r = k-1)
        #reverse rest of the elements
        helper(l = k , r = len(nums) - 1)
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol = Solution()
    sol.rotate(nums, k)
    print(nums)        