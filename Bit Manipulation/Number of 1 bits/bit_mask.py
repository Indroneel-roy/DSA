#problem link : https://leetcode.com/problems/number-of-1-bits/description/
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res    
if __name__ == "__main__":
    n = 2147483645
    sol = Solution()
    print(sol.hammingWeight(n))    