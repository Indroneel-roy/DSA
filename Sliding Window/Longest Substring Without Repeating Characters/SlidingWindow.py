# Problem Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        CharSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in CharSet:
                CharSet.remove(s[l])
                l += 1
            CharSet.add(s[r])
            res = max(res, r-l+1)
        return res   
if __name__ == "__main__":
    s = "pwwkew"
    sol = Solution()
    res = sol.lengthOfLongestSubstring(s)
    print(res)    