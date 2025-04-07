from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        
        for i in range(n):
            curr = 0
            
            for j in range(i, n):
                curr += nums[j]
                res = max(curr, res)
        return res

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(nums))             
                