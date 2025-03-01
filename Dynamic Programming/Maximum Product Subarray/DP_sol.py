from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
                continue
            tem = currMax*n
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(tem, n*currMin, n)
            res = max(res, currMax)
        return res       

if __name__ == "__main__":
    nums = [1,2,-3,4]   
    sol = Solution()
    print(sol.maxProduct(nums))  
        