#problem link : https://leetcode.com/problems/number-of-1-bits/description/
class Solution:
    def hammingWeight(self, n: int) -> int:
        count_ones = bin(n).count('1')
        return count_ones
if __name__ == "__main__":
    n = 2147483645
    sol = Solution()
    print(sol.hammingWeight(n))    