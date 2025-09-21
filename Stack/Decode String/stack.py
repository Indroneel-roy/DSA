# Problem Link : https://leetcode.com/problems/simplify-path/
from typing import List
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subStr = ''
                while stack[-1] != '[':
                    subStr = stack.pop() + subStr
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * subStr)
        return "".join(stack)                
if __name__ == "__main__":
    obj = Solution()
    print(obj.decodeString("3[a]2[bc]")) # return "aaabcbc"
    print(obj.decodeString("3[a2[c]]"))  # return "accaccacc"
    print(obj.decodeString("2[abc]3[cd]ef"))  # return "abcabccdcdcdef"
    print(obj.decodeString("abc3[cd]xyz"))  # return "abccdcdcdxyz"