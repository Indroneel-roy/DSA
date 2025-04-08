from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return 1000000

            res = 10000000    
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                res = min(res, 1 + dfs(j))
            memo[i] = res
            return res
        return dfs(0)    

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    s = Solution()
    print(s.jump(nums))     
    
# time complexity O(n**2)
#Space complexity O(n)        