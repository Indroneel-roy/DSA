#Problem Link : https://leetcode.com/problems/minimum-window-substring/description/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {}, {}
        for a in t:
            countT[a] = 1 + countT.get(a, 0)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0) 
            if c in countT and countT[c] == window[c]:
                have += 1
            while have == need:
                # update the res and resLen value
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # poping the value of left pointer
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""      

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"    
    sol = Solution()
    res = sol.minWindow(s, t)
    print(res)