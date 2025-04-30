#Problem Link :https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)                
