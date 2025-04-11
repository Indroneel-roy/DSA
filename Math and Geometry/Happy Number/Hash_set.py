class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquare(n)
            if n == 1:
                return True
        return False

    def sumOfSquare(self, n : int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output    

if __name__ == "__main__":
    n = 19
    s = Solution()
    print(s.isHappy(n))    