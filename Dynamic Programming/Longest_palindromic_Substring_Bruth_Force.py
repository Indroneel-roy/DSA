class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[i] == s[j]:
                    l += 1
                    r -= 1
                
                if l >= r and resLen < (j-i+1):
                    res = s[i:j+1]
                    resLen = j-i+1
        return res
    

if __name__ == "__main__":
    s = "ababd"
    long = Solution()
    p = long.longestPalindrome(s)
    print(p)