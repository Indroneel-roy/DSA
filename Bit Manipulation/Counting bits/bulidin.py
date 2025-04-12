# Problem Link : https://leetcode.com/problems/counting-bits/
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            c = bin(i).count("1")
            res.append(c)
        return res 
if __name__ == "__main__":
    n = 10
    sol = Solution()
    result = sol.countBits(n)
    print(result)       
        