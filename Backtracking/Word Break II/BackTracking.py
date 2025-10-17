# Problem Link : https://leetcode.com/problems/word-break-ii/description/
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cur = []
        res = []
        def BackTracking(i):
            if i == len(s):
                res.append(" ".join(cur))
                return
            for j in range(i, len(s)):
                w = s[i : j + 1]
                if w in wordDict:
                    cur.append(w)
                    BackTracking(j + 1)
                    cur.pop()
        BackTracking(0)
        return res                
if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))