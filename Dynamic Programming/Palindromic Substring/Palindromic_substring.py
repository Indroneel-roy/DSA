class Solution:
    def countSubstring(self, s : str) -> int:
        res = 0 
        for i in range(len(s)):
            # odd palindromic counpt 
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # Even palindromic count
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

if __name__ == "__main__":
    s = "aaab"
    palin = Solution()
    s = palin.countSubstring(s)
    print(s)