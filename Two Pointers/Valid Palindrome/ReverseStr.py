class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    sol = Solution()
    res = sol.isPalindrome(s)
    print(res)            