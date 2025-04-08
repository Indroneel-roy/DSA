from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res = 0
        total = 0
        for i in range(len(cost)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        return res            
        
if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]   
    s = Solution()
    print(s.canCompleteCircuit(gas, cost))     