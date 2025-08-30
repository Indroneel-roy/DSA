# Problem Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit        

if __name__ == "__main__":
    prices = [7,1,5,3,6,4, 20, 23]
    sol = Solution()
    print(sol.maxProfit(prices))
    
        