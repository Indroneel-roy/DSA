# Problem Link : https://leetcode.com/problems/longest-common-prefix/description/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]        

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))
    print(strs[0])        
        