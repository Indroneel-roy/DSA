from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res    
        
if __name__ == "__main__":
    nums = [4,1,2,1,2]
    sol = Solution()
    result = sol.singleNumber(nums=nums)
    print(result)        