#Problem Link :https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        for sell in prices:
            maxProfit = max(maxProfit, sell - minBuy )
            minBuy = min(minBuy, sell)
        return maxProfit    

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)      