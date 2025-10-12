# Problem Link : https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backTracking(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start, n + 1):
                comb.append(i)
                backTracking(i + 1, comb)
                comb.pop()
        backTracking(1, [])
        return res      
if __name__ == "__main__":
    obj = Solution()
    # Example 1
    n = 4
    k = 2
    print(obj.combine(n, k)) # return [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    # Example 2
    n = 1
    k = 1
    print(obj.combine(n, k)) # return [[1]]    