from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       
        def dfs(amount):
            if amount == 0:
                return 0
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
                    
            return res
        minCoin = dfs(amount)
        return -1 if minCoin >= 1e9 else minCoin
if __name__ == "__main__":
    conins = [1,2,3,4,5] 
    amount = 7
    sol = Solution()
    print(sol.coinChange(coins=conins, amount=amount))                
        