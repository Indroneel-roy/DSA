# Problem Link : https://leetcode.com/problems/reverse-string/description/
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
if __name__ == "__main__":
    s = ["H","a","n","n","a","h"]
    sol = Solution()
    print(sol.reverseString(s))
    print(s)
