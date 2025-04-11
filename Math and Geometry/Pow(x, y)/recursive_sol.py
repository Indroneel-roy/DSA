class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x*x, n // 2)
            return x * res if n % 2 else res
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res           
    
if __name__ == "__main__":
    x = 10
    n = 5
    s = Solution()
    res = s.myPow(x, n)
    print(res)
            