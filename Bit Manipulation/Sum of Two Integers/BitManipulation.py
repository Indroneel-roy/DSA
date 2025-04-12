# Problem Link : https://leetcode.com/problems/sum-of-two-integers/description/
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)
if __name__ == "__main__":
    a = 23
    b = -2
    sol =  Solution()
    result = sol.getSum(a, b)
    print(result)        