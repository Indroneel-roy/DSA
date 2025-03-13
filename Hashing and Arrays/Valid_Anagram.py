class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if s_sorted == t_sorted:
            return True
        return False    
if __name__ == "__main__":
    s = "add"
    t = "dda"
    sol = Solution()
    result = sol.isAnagram(s,t)
    print(result)    