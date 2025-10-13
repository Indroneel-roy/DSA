# problem link : https://leetcode.com/problems/permutations-ii/description/
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        prem = []
        count = { n : 0 for n in nums}
        for n in nums:
            count[n] += 1
        def dfs():
            if len(prem) == len(nums):
                res.append(prem.copy())
                return 
            for n in count:
                if count[n] > 0:
                    prem.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    prem.pop()
        dfs()
        return res                    
if __name__ == "__main__":
    obj = Solution()
    # Example 1
    nums = [1,1,2]
    print(obj.permuteUnique(nums)) # return [[1,1,2],[1,2,1],[2,1,1]]
    # Example 2
    nums = [1,2,3]
    print(obj.permuteUnique(nums)) # return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]