#Problem Link : https://leetcode.com/problems/car-fleet/description/
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)        

if __name__ == "__main__":
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]    
    sol = Solution()
    res = sol.carFleet(target, position, speed)
    print(res)