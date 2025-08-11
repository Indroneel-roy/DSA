# Problem Link : https://leetcode.com/problems/palindrome-partitioning/description/
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPlindrom(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    
    def isPlindrom(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True   
    
if __name__ == "__main__":
    s = "aab"
    sol = Solution()
    print(sol.partition(s))        