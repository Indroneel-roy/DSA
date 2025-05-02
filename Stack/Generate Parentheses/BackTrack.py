#Problem Link : https://leetcode.com/problems/generate-parentheses/description/
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()

            if openN > closeN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0, 0)
        return res    

if __name__ == "__main__":
    n = 5
    sol = Solution()
    res = sol.generateParenthesis(n)
    print(res)    