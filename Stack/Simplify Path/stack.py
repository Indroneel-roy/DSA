# Problem Link : https://leetcode.com/problems/simplify-path/
from typing import List
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for curr in path.split("/"):
            if curr == "..":
                if stack:
                    stack.pop()
            elif curr != "." and curr != "":
                stack.append(curr)
        return "/" + "/".join(stack)       
if __name__ == "__main__":
    obj = Solution()
    print(obj.simplifyPath("/home/")) # return "/home"
    print(obj.simplifyPath("/../"))  # return "/"
    print(obj.simplifyPath("/home//foo/"))  # return "/home/foo"
    print(obj.simplifyPath("/a/./b/../../c/"))  # return "/c"
    print(obj.simplifyPath("/a/../../b/../c//.//"))  # return "/c"
    print(obj.simplifyPath("/a//b////c/d//././/.."))  # return "/a/b/c"    