from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0
        for i in range(len(nums)):
            if curr < 0 :
                curr = 0
            curr += nums[i]
            res = max(res, curr)
        return res
    
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(nums))        

# Time complexity is O(n)
# Space complexity is O(1)                