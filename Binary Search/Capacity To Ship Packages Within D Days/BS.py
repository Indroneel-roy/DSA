# problem Link : https://leetcode.com/problems/search-insert-position/
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        def capShip(cap):
            ship, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ship += 1
                    currCap = cap
                currCap = currCap - w    
            return ship <= days

        while l <= r:
            mid = (l + r) // 2
            if capShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res                    
if __name__ == "__main__":
    obj = Solution()
    print(obj.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)) # return 15
    print(obj.shipWithinDays([3,2,2,4,1,4], 3))          # return 6
    print(obj.shipWithinDays([1,2,3,1,1], 4))            # return 3