# Problem Link : https://leetcode.com/problems/reverse-bits/description/
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res

if __name__ == "__main__":
    n = 45
    sol = Solution()
    res = sol.reverseBits(n)
    print(res)          