#Problem Link : https://leetcode.com/problems/valid-palindrome/
# This is a space optimize solution that don't take any extra memorey. Space complexity O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.alNum(s[l]):
                l += 1
            while r > l and not self.alNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True            
        
    
    
    def alNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))    

if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    sol = Solution()
    res = sol.isPalindrome(s)
    print(res)          