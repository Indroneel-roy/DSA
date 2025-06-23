# Problem Link : https://leetcode.com/problems/subsets/description/
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return 
            curr.append(nums[i]) # including i
            dfs(i + 1)

            curr.pop()  #excluding i
            dfs(i + 1)
        dfs(0)
        return res    

if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.subsets(nums))     