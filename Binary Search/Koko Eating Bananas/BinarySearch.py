# Problem Link : https://leetcode.com/problems/koko-eating-bananas/description/
#time complexity O(n*logm)
from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
       
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
        
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res                
        
if __name__ == "__main__":
    piles = [30,11,23,4,20]
    h = 5
    sol = Solution()
    res = sol.minEatingSpeed(piles, h)
    print(res)        