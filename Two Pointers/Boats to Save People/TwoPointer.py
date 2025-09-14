# Problem Link : https://leetcode.com/problems/boats-to-save-people/description/
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            remaining_w = limit - people[r]
            r -= 1
            boats += 1
            if l <= r and remaining_w >= people[l]:
                l += 1
        return boats        
        
if __name__ == "__main__":
    people = [3,2,2,1]
    limit = 3
    sol = Solution()
    print(sol.numRescueBoats(people, limit))        