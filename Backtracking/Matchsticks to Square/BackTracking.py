# Problem Link : https://leetcode.com/problems/matchsticks-to-square/description/
from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        if length != sum(matchsticks) / 4:
            return False
        side = [0] * 4
        matchsticks.sort(reverse = True)
        def backTracking(i):
            if i == len(matchsticks):
                return True
            for j in range(4):

                if side[j] + matchsticks[i] <= length:
                    side[j] += matchsticks[i] 
                    if backTracking(i + 1):
                        return True
                    side[j] -= matchsticks[i]
            return False
        return backTracking(0)                
if __name__ == "__main__":
    matchsticks = [1,1,2,2,2]
    sol = Solution()
    print(sol.makesquare(matchsticks))