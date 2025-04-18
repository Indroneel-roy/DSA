# Problem Link : https://leetcode.com/problems/counting-bits/
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp
if __name__ == "__main__":
    n = 10
    sol = Solution()
    result = sol.countBits(n)
    print(result)       
                    