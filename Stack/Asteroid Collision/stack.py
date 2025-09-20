# Porblem Link : https://leetcode.com/problems/asteroid-collision/
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack    
if __name__ == "__main__":
    obj = Solution()
    print(obj.asteroidCollision([5,10,-5])) # [5,10]
    print(obj.asteroidCollision([8,-8]))    # []
    print(obj.asteroidCollision([10,2,-5]))  # [10]
    print(obj.asteroidCollision([-2,-1,1,2]))# [-2,-1,1,2]    
