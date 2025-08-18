from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        n = len(nums)
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans    
if __name__ == "__main__":
    nums = [1,3,2,1]
    sol = Solution()
    print(sol.getConcatenation(nums))
         