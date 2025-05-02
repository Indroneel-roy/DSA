#Problem Link : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/": 
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(c))
        return stack[0]     

if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    sol = Solution()
    res = sol.evalRPN(tokens)
    print(res)    