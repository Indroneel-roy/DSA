# problem link : https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < temPrices[d]:
                    temPrices[d] = prices[s] + p
            prices = temPrices
        return -1 if prices[dst] == float('inf') else prices[dst]     
    
if __name__ == "__main__":
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    sol = Solution()
    result = sol.findCheapestPrice(n, flights, src, dst, k)
    print(f"Cheapest price from {src} to {dst} with at most {k} stops is: {result}")    