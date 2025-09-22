# Problem Link : https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 1, x//2
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r                    
if __name__ == "__main__":
    obj = Solution()
    print(obj.mySqrt(4))  # return 2
    print(obj.mySqrt(8))  # return 2
    print(obj.mySqrt(0))  # return 0
    print(obj.mySqrt(1))  # return 1
    print(obj.mySqrt(2147395599))  # return 46339    