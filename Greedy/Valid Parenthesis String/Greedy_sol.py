class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        
        for c in s:
            if c == "(":
                leftMax, leftMin = leftMax + 1, leftMin + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMax, leftMin = leftMax + 1, leftMin - 1
            
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
if __name__ == "__main__":
    s = "(*))"
    sol = Solution()
    print(sol.checkValidString(s))                        