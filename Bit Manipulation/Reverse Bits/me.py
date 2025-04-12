# Problem Link : https://leetcode.com/problems/reverse-bits/description/
class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:].zfill(32)
        reverse = binary_str[::-1]
        output = int(reverse, 2)
        return output
if __name__ == "__main__":
    n = 45
    sol = Solution()
    res = sol.reverseBits(n)
    print(res)    